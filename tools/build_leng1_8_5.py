# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.5 · Proyecto final: «Mi historia, mis metas».
Fuente: clases_leng1/clase_8-5.html (GEDparaHispanos), adaptada al marco de LearnGED.
Añade un cuaderno del proyecto en la propia página: los textos con contador de palabras, la gráfica que se dibuja sola con
los datos del estudiante, la lista de verificación y la impresión en PDF. Todo se guarda en el navegador (localStorage).
Uso: python3 tools/build_leng1_8_5.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-5"
COMP = ["Texto escrito", "Gráfica", "Presentación oral", "Uso de tecnología", "Revisión"]
ANA_HIST = ["Nací en Puebla, México, en 1975. Desde niña me gustó la escuela, pero a los catorce años tuve que dejar los estudios para ayudar a mi familia. Trabajé en la tienda de mis padres durante muchos años. En 2003 me casé y, dos años después, mi esposo y yo decidimos emigrar a Chicago en busca de mejores oportunidades para nuestros futuros hijos.",
            "Durante quince años trabajé en una panadería del barrio de Pilsen. Tuve dos hijos, Mateo y Sofía, y los crie sola los últimos cinco años, después de quedar viuda. Mis hijos terminaron la high school el año pasado y ahora estudian en un colegio comunitario. Verlos avanzar me dio el valor para regresar yo también a las aulas."]
ANA_METAS = ["Hoy estudio el Nivel 1 de Artes del Lenguaje para preparar el GED en español. Mi primera meta es terminar los cuatro niveles y aprobar el GED en dos años. Mi segunda meta es entrar a un programa de asistente médico, una carrera corta, para trabajar en una clínica del barrio.",
             "A largo plazo, sueño con dar charlas en mi iglesia a otras mujeres hispanas que, como yo, dejaron los estudios y creen que es tarde para volver. Les voy a decir lo que ahora sé: nunca es tarde, y cada día en clase es un paso hacia adelante."]
HORAS = [("Enero", 8), ("Febrero", 12), ("Marzo", 15), ("Abril", 18), ("Mayo", 22)]
# Preguntas tipo GED sobre el modelo: (pregunta, correcta, distractores, explicación)
GED = [("¿Cuál es la idea principal del proyecto de Ana?", "Nunca es tarde para volver a estudiar y cumplir metas.", ["Ana trabajó quince años en una panadería.", "Pilsen es un barrio de Chicago."], "Las demás son detalles; la idea que une todo es que nunca es tarde."),
       ("¿Por qué dejó Ana la escuela?", "Para ayudar a su familia.", ["Porque no le gustaba estudiar.", "Porque emigró a Chicago."], "Lo dice el primer párrafo: «tuve que dejar los estudios para ayudar a mi familia»."),
       ("¿Qué le dio a Ana el valor para regresar a estudiar?", "Ver avanzar a sus hijos.", ["Perder su trabajo.", "Un consejo de su iglesia."], "«Verlos avanzar me dio el valor para regresar yo también a las aulas.»"),
       ("Según la gráfica, ¿cuántas horas estudió Ana por semana en marzo?", "15", ["12", "18"], "La barra de marzo llega a 15."),
       ("¿Qué muestra la gráfica en conjunto?", "Ana estudia cada mes más horas por semana.", ["Ana estudia cada mes menos horas.", "Ana estudia siempre las mismas horas."], "Las barras suben de 8 a 22 horas."),
       ("¿Cuál es la meta de Ana a largo plazo?", "Dar charlas a otras mujeres hispanas.", ["Aprobar el GED en dos años.", "Trabajar en una panadería."], "Aprobar el GED es su meta a mediano plazo; las charlas son a largo plazo."),
       ("¿Qué palabra describe mejor a Ana, según el texto?", "Perseverante", ["Perezosa", "Indecisa"], "Siguió adelante pese a las dificultades y volvió a estudiar."),
       ("¿En qué orden organiza Ana su texto?", "Pasado, presente y futuro", ["Futuro, pasado y presente", "Solo habla del presente"], "Cuenta de dónde viene, dónde está y a dónde va.")]
QUE = [("Escribir 200 a 300 palabras sobre su historia y sus metas.", 0), ("Organizar las ideas en pasado, presente y futuro.", 0), ("Hacer una gráfica de barras con sus horas de estudio.", 1),
       ("Poner título y ejes a la gráfica.", 1), ("Grabarse con el teléfono diciendo el guion.", 2), ("Ensayar tres veces con el cronómetro.", 2),
       ("Pasar el texto al teléfono o a la computadora.", 3), ("Guardar el texto, la gráfica y el video en una carpeta con nombres claros.", 3),
       ("Corregir el borrador con la lista de la Lección 7.6.", 4), ("Pedir a alguien que lea el texto y anotar qué cambió.", 4)]
LISTA = ["Mi texto tiene entre 200 y 300 palabras, en pasado, presente y futuro.", "Revisé la ortografía y la puntuación con la lista de la Lección 7.6.",
         "Mi gráfica tiene título, ejes y datos claros.", "Los datos de mi gráfica son míos y reales.", "Preparé mi guion con apertura, desarrollo y cierre.",
         "Ensayé al menos tres veces en voz alta y me grabé.", "Pasé mi texto al teléfono o a la computadora y lo guardé con un nombre claro.",
         "Guardé el texto, la gráfica y la grabación juntos en una carpeta.", "Pedí a alguien que leyera mi texto o viera mi presentación (si fue posible).", "Hice al menos tres mejoras y anoté cuáles."]

CUADERNO = """<div class="cuaderno-proy" id="proyecto">
<p class="nota-fina">Lo que escriba aquí se guarda solo en este navegador, en este aparato. Para conservarlo, use «Imprimir o guardar en PDF».</p>
<label for="pr-nombre"><strong>Mi nombre</strong></label><input type="text" id="pr-nombre" data-g="nombre" autocomplete="name">
<label for="pr-hist"><strong>Mi historia</strong> (de dónde vengo y dónde estoy)</label><textarea id="pr-hist" data-g="hist" rows="7"></textarea>
<label for="pr-metas"><strong>Mis metas</strong> (a dónde quiero llegar: una meta cercana y una lejana)</label><textarea id="pr-metas" data-g="metas" rows="6"></textarea>
<p class="pr-cuenta" id="pr-cuenta" aria-live="polite">0 palabras · meta: de 200 a 300</p>
<fieldset class="pr-graf"><legend><strong>Mi gráfica</strong></legend>
<label for="pr-gtit">Título</label><input type="text" id="pr-gtit" data-g="gtit" placeholder="Ej.: Mis horas de estudio por semana">
<label for="pr-gy">¿Qué se mide? (eje vertical)</label><input type="text" id="pr-gy" data-g="gy" placeholder="Ej.: Horas">
<table class="tabla-ej"><thead><tr><th scope="col">Categoría (eje horizontal)</th><th scope="col">Valor</th></tr></thead><tbody id="pr-filas"></tbody></table>
<div id="pr-svg" class="pr-svg"></div></fieldset>
<fieldset><legend><strong>Lista de verificación</strong></legend><div id="pr-lista"></div><p id="pr-listac" aria-live="polite"></p></fieldset>
<p><button type="button" class="btn" id="pr-imp">🖨️ Imprimir o guardar en PDF</button> <button type="button" class="btn-sec" id="pr-borrar">Borrar todo</button></p></div>
<script>(function(){var K="learnged-proyecto-n1",D={};try{D=JSON.parse(localStorage.getItem(K)||"{}");}catch(e){D={};}
function g(){try{localStorage.setItem(K,JSON.stringify(D));}catch(e){}}
var LISTA=__LISTA__,cont=document.getElementById("proyecto");
var fb=document.getElementById("pr-filas");for(var i=0;i<6;i++){fb.insertAdjacentHTML("beforeend",'<tr><td><input type="text" data-g="c'+i+'" aria-label="Categoría '+(i+1)+'"></td><td><input type="number" min="0" data-g="v'+i+'" aria-label="Valor '+(i+1)+'"></td></tr>');}
var li=document.getElementById("pr-lista");LISTA.forEach(function(t,i){li.insertAdjacentHTML("beforeend",'<label class="pr-ck"><input type="checkbox" data-g="k'+i+'"> '+t+'</label>');});
cont.querySelectorAll("[data-g]").forEach(function(el){var k=el.getAttribute("data-g");if(D[k]!==undefined){if(el.type==="checkbox")el.checked=!!D[k];else el.value=D[k];}
el.addEventListener("input",function(){D[k]=el.type==="checkbox"?el.checked:el.value;g();pinta();});el.addEventListener("change",function(){D[k]=el.type==="checkbox"?el.checked:el.value;g();pinta();});});
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
function pinta(){var txt=(D.hist||"")+" "+(D.metas||""),n=(txt.trim().match(/\\S+/g)||[]).length,c=document.getElementById("pr-cuenta");
c.textContent=n+" palabras · meta: de 200 a 300"+(n<200?" (le faltan "+(200-n)+")":n>300?" (le sobran "+(n-300)+")":" ✓");
var d=[];for(var i=0;i<6;i++){var v=parseFloat(D["v"+i]);if(D["c"+i]&&!isNaN(v))d.push([D["c"+i],v]);}
var box=document.getElementById("pr-svg");if(!d.length){box.innerHTML='<p class="nota-fina">Escriba al menos una categoría y su valor para ver la gráfica.</p>';}
else{var W=520,H=300,ml=56,mb=50,mt=30,max=Math.max.apply(null,d.map(function(x){return x[1];}))||1,paso=Math.pow(10,Math.floor(Math.log10(max)));if(max/paso<3)paso/=2;var top=Math.ceil(max/paso)*paso,ih=H-mt-mb,bw=(W-ml-20)/d.length;
var s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Gráfica de barras: '+esc(D.gtit||"Mi gráfica")+'. '+d.map(function(x){return esc(x[0])+", "+x[1];}).join("; ")+'" style="width:100%;max-width:520px">';
s+='<text x="'+(W/2)+'" y="18" text-anchor="middle" font-size="16" font-weight="800">'+esc(D.gtit||"")+'</text>';
for(var y=0;y<=top+1e-9;y+=paso){var yy=mt+ih-y/top*ih;s+='<line x1="'+ml+'" x2="'+(W-20)+'" y1="'+yy+'" y2="'+yy+'" stroke="#e1e6ea"/><text x="'+(ml-6)+'" y="'+(yy+4)+'" text-anchor="end" font-size="12">'+(+y.toFixed(2))+'</text>';}
d.forEach(function(x,i){var h=x[1]/top*ih,xx=ml+i*bw+bw*.18;s+='<rect x="'+xx+'" y="'+(mt+ih-h)+'" width="'+(bw*.64)+'" height="'+h+'" fill="#0b679c"/><text x="'+(xx+bw*.32)+'" y="'+(mt+ih-h-5)+'" text-anchor="middle" font-size="12" font-weight="700">'+x[1]+'</text><text x="'+(xx+bw*.32)+'" y="'+(mt+ih+16)+'" text-anchor="middle" font-size="12">'+esc(x[0])+'</text>';});
s+='<line x1="'+ml+'" x2="'+ml+'" y1="'+mt+'" y2="'+(mt+ih)+'" stroke="#1a2330"/><line x1="'+ml+'" x2="'+(W-20)+'" y1="'+(mt+ih)+'" y2="'+(mt+ih)+'" stroke="#1a2330"/>';
s+='<text x="14" y="'+(mt+ih/2)+'" text-anchor="middle" font-size="13" font-weight="700" transform="rotate(-90 14 '+(mt+ih/2)+')">'+esc(D.gy||"")+'</text></svg>';box.innerHTML=s;}
var k=0;for(var j=0;j<LISTA.length;j++)if(D["k"+j])k++;document.getElementById("pr-listac").textContent="Pasos completados: "+k+" de "+LISTA.length;}
document.getElementById("pr-imp").addEventListener("click",function(){document.querySelectorAll("details").forEach(function(x){x.open=true;});window.print();});
document.getElementById("pr-borrar").addEventListener("click",function(){var b=this;if(b.getAttribute("data-conf")!=="1"){b.setAttribute("data-conf","1");b.textContent="¿Seguro? Pulse otra vez para borrar";return;}
D={};g();cont.querySelectorAll("[data-g]").forEach(function(el){if(el.type==="checkbox")el.checked=false;else el.value="";});b.removeAttribute("data-conf");b.textContent="Borrar todo";pinta();});
pinta();})();</script>"""


def barras(tit, xe, ye, dat):
    spec = {"tipo": "barras", "xEtq": xe, "yEtq": ye, "py": 5, "barras": [{"etq": c, "valor": v} for c, v in dat]}
    desc = f"Gráfica de barras: {tit}. " + "; ".join(f"{c}, {v}" for c, v in dat) + "."
    return f'<figure class="figura grafica"><figcaption class="graf-tit">{tit}</figcaption>{C.grafica(spec, desc, ancho=520, alto=300)}</figure>'


def leccion():
    P = C.Practicas()
    import json
    s1 = f"""<p>Llegó al proyecto final del Nivel 1. Aquí reúne lo que aprendió: leer, escribir, hacer una gráfica, usar la tecnología, presentar en voz alta y revisar. El proyecto es personal: <strong>«Mi historia, mis metas»</strong>. Puede trabajarlo en varios días.</p>
{C.tabla("Los cinco componentes", ["Componente", "Qué es", "Lo aprendió en…"],
         [["📝 1 · Texto escrito", "De 200 a 300 palabras sobre su historia y sus metas.", "Tema 7"], ["📊 2 · Gráfica", "Una gráfica sencilla con datos suyos y reales.", "Tema 6"],
          ["🎤 3 · Presentación oral", "De 3 a 4 minutos, grabada con el teléfono o ante alguien de su casa.", "Lección 8.4"],
          ["💻 4 · Tecnología", "Pasar el texto al teléfono o a la computadora y guardar todo en una carpeta con nombres claros.", "Lección 8.3"],
          ["🔄 5 · Revisión", "Revisar el borrador y hacer una versión final.", "Lección 7.6"]])}
{P("Compruebe", "Guardar el texto, la gráfica y el video en una carpeta con nombres claros es el componente de…", COMP, 3, {0: "No es escribir.", 1: "No es hacer la gráfica.", 2: "No es presentar.", 4: "No es revisar."}, "<strong>Uso de tecnología.</strong>")}"""

    s2 = f"""<p>Ana Rodríguez es un personaje inventado, pero su historia se parece a la de muchas personas. Lea el modelo completo una vez, sin detenerse.</p>
<div class="texto-lectura"><p><strong>Mi historia, mis metas</strong> · por Ana Rodríguez (personaje de ejemplo)</p>{"".join(f"<p>{p}</p>" for p in ANA_HIST + ANA_METAS)}</div>
{barras("Mis horas de estudio por semana", "Mes", "Horas por semana", HORAS)}
<p class="nota-fina">Datos de ejemplo: registro personal de Ana (de enero a mayo).</p>
<div class="texto-lectura"><p><strong>🚀 Apertura:</strong> «Buenas tardes. Soy Ana Rodríguez y hoy quiero contarles mi historia: de dónde vengo, dónde estoy y a dónde voy.»</p>
<p><strong>💡 Desarrollo:</strong> mi historia en Puebla; los quince años de panadería; el regreso a las aulas con el ejemplo de mis hijos. Aquí muestra la gráfica.</p>
<p><strong>🎯 Cierre:</strong> «Vengo de lejos, estoy avanzando y voy a ser asistente médica. Si yo puedo, ustedes también pueden. Muchas gracias.»</p></div>
<h3>Preguntas tipo GED sobre el modelo</h3>
<p>El examen GED hace preguntas sobre textos y gráficas. Estas siguen ese formato, a nivel básico.</p>
{"".join(P(f"Pregunta {i + 1}", q, [ok] + d, 0, {1: "Vuelva al texto: no es lo que dice.", 2: "Vuelva al texto: no es lo que dice."}, f"<strong>{ok}</strong> {e}") for i, (q, ok, d, e) in enumerate(GED[:5]))}
<h3>Qué hace bien el modelo</h3>
<ul><li><strong>Estructura en tres tiempos:</strong> pasado, presente y futuro.</li><li><strong>Datos concretos:</strong> no dice «trabajé muchos años», dice «quince años en una panadería de Pilsen».</li>
<li><strong>Una gráfica que apoya:</strong> muestra el aumento real de horas de estudio, no adorna.</li><li><strong>Metas en dos plazos:</strong> el GED (cercana) y las charlas (lejana).</li>
<li><strong>Un cierre con mensaje:</strong> «si yo puedo, ustedes también pueden».</li></ul>"""

    s3 = f"""{C.tabla("Rúbrica del proyecto (20 puntos)", ["Criterio", "1 · Inicial", "2 · En desarrollo", "3 · Competente", "4 · Avanzado"],
         [["Texto escrito", "Oraciones sueltas, sin orden.", "Hay orden, pero faltan conectores o ejemplos.", "Bien estructurado, con buenos ejemplos.", "Sólido, organizado y con datos concretos."],
          ["Gráfica", "No hay gráfica o está vacía.", "Sin título o sin datos claros.", "Correcta, con título y datos legibles.", "Clara, bien titulada y conectada con el texto."],
          ["Presentación oral", "No se entiende o lee todo.", "Se entiende a ratos; depende del papel.", "Buen volumen y ritmo, mira al público.", "Habla con claridad, controla la voz y mantiene la atención."],
          ["Tecnología", "Todo quedó en papel.", "Pasó el texto, pero no lo guardó bien.", "Guardó el texto con un nombre claro y grabó la presentación.", "Texto, gráfica y video juntos en una carpeta con nombres claros."],
          ["Revisión", "Primer borrador sin revisar.", "Corrigió algunos errores.", "Revisó con la lista de la 7.6 y corrigió casi todo.", "Usó la lista y los comentarios de otra persona, y anotó qué cambió."]])}
{C.caja("tip", "Cómo usar la rúbrica", "<p>Léala <strong>antes</strong> de empezar: el nivel «Avanzado» de cada criterio es su objetivo. Una buena meta es llegar al menos a 12 puntos.</p>")}
<h3>El cuaderno de mi proyecto</h3>
{CUADERNO.replace("__LISTA__", json.dumps(LISTA, ensure_ascii=False))}"""

    secciones = [("s1", "Los cinco componentes", s1), ("s2", "Un proyecto modelo", s2), ("s3", "La rúbrica y el cuaderno de mi proyecto", s3)]
    tarea = [("Mi texto.", "Escriba su historia y sus metas en el cuaderno del proyecto (o en papel): de 200 a 300 palabras, en pasado, presente y futuro."),
             ("Mi gráfica.", "Elija datos suyos y reales (horas de estudio, gastos, pasos al día…) y hágala en el cuaderno del proyecto."),
             ("Mi guion y mi video.", "Prepare el guion con la plantilla de la Lección 8.4, ensaye y grábese."),
             ("Mi carpeta.", "Guarde el PDF del cuaderno, la foto o captura de la gráfica y el video en una carpeta llamada «Proyecto Nivel 1»."),
             ("Mi revisión.", "Revise con la lista de la 7.6, pida comentarios si puede y anote tres cambios que hizo.")]
    quiz = [
        ("¿Cuántos componentes tiene el proyecto?", ["Cinco", "Tres", "Diez"], 0, {1: "Cuente: texto, gráfica, presentación, tecnología y revisión.", 2: "Diez son los pasos de la lista."}, "<strong>Cinco.</strong>"),
        ("¿Cuántas palabras debe tener el texto?", ["De 200 a 300", "De 20 a 30", "Más de 1,000"], 0, {1: "Muy poco.", 2: "Demasiado."}, "<strong>De 200 a 300.</strong>"),
        ("¿En qué orden conviene organizar el texto?", ["Pasado, presente y futuro", "Futuro, pasado y presente"], 0, {}, "<strong>Pasado, presente y futuro.</strong>"),
        ("¿Cómo deben ser los datos de la gráfica?", ["Suyos y reales", "Inventados"], 0, {}, "<strong>Suyos y reales.</strong>"),
        (GED[5][0], [GED[5][1]] + GED[5][2], 0, {1: "Esa es la meta cercana.", 2: "Eso es su pasado."}, f"<strong>{GED[5][1]}</strong>"),
        (GED[6][0], [GED[6][1]] + GED[6][2], 0, {1: "No: trabajó y volvió a estudiar.", 2: "No: tiene metas claras."}, f"<strong>{GED[6][1]}</strong>: {GED[6][3]}"),
        ("¿Por qué el modelo de Ana usa datos concretos?", ["Hacen la historia creíble y memorable", "Para alargar el texto"], 0, {}, "La hacen <strong>creíble y memorable</strong>."),
        ("¿Cuántos puntos tiene la rúbrica en total?", ["20", "10", "100"], 0, {1: "Son cinco criterios de 4 puntos.", 2: "No."}, "<strong>20</strong>: cinco criterios de 4 puntos."),
        ("¿Cuándo conviene leer la rúbrica?", ["Antes de empezar", "Después de terminar"], 0, {}, "<strong>Antes</strong>: le da un objetivo."),
        ("¿Dónde se guarda lo que escribe en el cuaderno del proyecto?", ["En este navegador; para conservarlo, se imprime o se guarda en PDF", "En la nube de LearnGED"], 0, {}, "<strong>En el navegador</strong>: guárdelo en PDF."),
    ]
    filas = [
        ("Texto y gráfica", "Mi texto tiene de 200 a 300 palabras y mi gráfica tiene título, ejes y datos reales.", "Tengo el texto, pero me falta la gráfica.", "Todavía no empiezo (<a href=\"#s3\">vaya al cuaderno del proyecto</a>)."),
        ("Presentación", "Me grabé con el guion de la 8.4.", "Ensayé, pero no me grabé.", "No preparé el guion (<a href=\"#s2\">mire el modelo</a>)."),
        ("Revisión y carpeta", "Revisé, anoté tres cambios y guardé todo en una carpeta.", "Revisé, pero no guardé todo junto.", "No revisé (<a href=\"#s3\">use la lista de verificación</a>)."),
    ]
    cierre = "<p>Con el proyecto listo, solo falta presentarlo. En la última lección del nivel va a hacer su <strong>presentación final, la evaluación del Nivel 1</strong> y a mirar el camino al GED.</p>"
    glosario = [("Proyecto integrador", "Trabajo que reúne lo aprendido en todo el nivel."), ("Rúbrica", "Tabla que dice qué se evalúa y cómo es cada nivel."),
                ("Meta a mediano plazo", "Lo que se quiere lograr en uno o dos años."), ("Meta a largo plazo", "Lo que se quiere lograr más adelante.")]
    conexion = ("<p>Ya sabe leer, escribir, hacer gráficas, usar la tecnología y presentar en voz alta. Ahora va a juntarlo todo en un proyecto personal.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, un teléfono o una computadora, y tiempo: puede trabajarlo en varios días.</p>")
    estd = LE.estandares(["R.2.1", "R.7.2", "W.1"], base=["W.2"], fund=["SL.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Todo lo aprendido, en un proyecto personal.", ["Proyecto final", "Integración"],
                            ["<strong>Escribir</strong> un texto de 200 a 300 palabras sobre su historia y sus metas.", "<strong>Hacer</strong> una gráfica con datos propios.",
                             "<strong>Preparar</strong> y grabar una presentación oral.", "<strong>Revisar</strong> el proyecto con una rúbrica y una lista de verificación."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-6", LE.titulo("8-6")), glosario, P)


def practica():
    g = barras("Mis horas de estudio por semana", "Mes", "Horas por semana", HORAS)
    texto = "<div class=\"texto-lectura\">" + "".join(f"<p>{p}</p>" for p in ANA_HIST + ANA_METAS) + "</div>"
    ged = [{"enun": (g if "gráfica" in q else texto) + q, "ops": [ok] + d, "ok": 0, "pista": "Vuelva al texto o a la gráfica y busque la respuesta.", "exp": f"<strong>{ok}</strong>. {e}"} for q, ok, d, e in GED]
    que = [{"enun": f"<strong>{t}</strong><br>¿A qué componente del proyecto corresponde?", "ops": COMP, "ok": k, "enOrden": True, "pista": "Texto, gráfica, presentación, tecnología o revisión.",
            "exp": f"Es del componente <strong>{COMP[k].lower()}</strong>."} for t, k in QUE]
    mods = [("ged", "Preguntas tipo GED sobre el modelo de Ana", C.om("m1", "Lea el texto o la gráfica de Ana y responda.")),
            ("componentes", "¿Qué componente es?", C.om("m2", "Decida a qué componente del proyecto corresponde cada tarea."))]
    js = C.js_datos("GED", ged) + C.js_datos("QUE", que) + 'creaBanco("m1", GED);\ncreaBanco("m2", QUE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Dos actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 4 horas, en varios días")
