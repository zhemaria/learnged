"""LearnGED · Ciencias · Lección 8.2 · Proyecto final: mi propia investigación (EN/ES).
Fuente: clases_ciencias/leccion_8-2.html (cuaderno de trabajo con campos, borrador en el navegador, informe e impresión).
Página única (sin página de práctica): el proyecto sustituye a la evaluación. Además de la plantilla original, la página
calcula la media de cada condición a partir de la tabla de datos y dibuja una gráfica de barras para revisarla.
Uso: python3 tools/build_sci_8_2.py
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "8-2"


def R(x):
    return f'<span class="raiz">{x}</span>'


def campo(fid, etiqueta, ayuda="", filas=4):
    ay = f'<p class="ayuda" id="{fid}-ayuda">{ayuda}</p>' if ayuda else ""
    desc = f' aria-describedby="{fid}-ayuda"' if ayuda else ""
    return f'<div class="campo"><label for="{fid}">{etiqueta}</label>{ay}<textarea id="{fid}" class="trabajo" rows="{filas}" data-campo="{fid}"{desc}></textarea></div>'


def etapa(n, sid, tit, cuerpo):
    return f'<section class="etapa"><h2 id="{sid}"><span aria-hidden="true" class="num-seccion">{n}</span>{tit}</h2>\n{cuerpo}\n</section>'


def pagina():
    L = C.L
    tn = 8
    rub = C.tabla(t("Final project rubric: five criteria, four levels, up to 20 points", "Rúbrica analítica del proyecto final con cinco criterios y cuatro niveles de desempeño, hasta un máximo de veinte puntos"),
        [t("Criterion", "Criterio"), t("Beginning (1)", "Inicial (1)"), t("Developing (2)", "En desarrollo (2)"), t("Proficient (3)", "Competente (3)"), t("Advanced (4)", "Destacado (4)")],
        [[t("1 · A question you can investigate and a testable hypothesis", "1 · Pregunta investigable e hipótesis comprobable"), t("The question cannot be answered by measuring.", "La pregunta no puede responderse con una medición."), t("The question can be investigated, but the hypothesis does not predict a specific result.", "La pregunta es investigable, pero la hipótesis no anticipa un resultado concreto."), t("The question is answered by measuring, and the hypothesis predicts a result that can be tested.", "La pregunta se responde midiendo y la hipótesis anticipa un resultado comprobable."), t("The hypothesis also names the variable that is changed and the one that is measured, and explains what it is based on.", "La hipótesis nombra además la variable que se cambia y la que se mide, y explica en qué se basa.")],
         [t("2 · Design with variables named and a fair control", "2 · Diseño con variables identificadas y control adecuado"), t("Does not separate what changes from what is measured.", "No distingue qué cambia y qué se mide."), t("Names the variables but does not keep the other conditions the same.", "Identifica las variables, pero no mantiene constantes las demás condiciones."), t("Isolates the independent variable and keeps the others the same.", "Aísla la variable independiente y mantiene constantes las demás."), t("Also adds a control group or repeated trials, and explains why they are needed.", "Incorpora además un grupo de control o repeticiones, y justifica su necesidad.")],
         [t("3 · Data in a table and the right kind of graph", "3 · Datos organizados en tabla y gráfica apropiada"), t("The data are scattered, not organized.", "Los datos aparecen sueltos, sin organizar."), t("There is a table, but the graph does not fit the data or has no labels.", "Hay tabla, pero la gráfica no corresponde al tipo de datos o carece de rótulos."), t("A complete table and the right kind of graph, with labeled axes and units.", "Tabla completa y gráfica del tipo adecuado, con ejes rotulados y unidades."), t("The graph can be read with no extra explanation, and the choice of graph is explained.", "La gráfica se lee sin explicación adicional y el tipo elegido se justifica.")],
         [t("4 · A conclusion that fits the data, with a limitation admitted", "4 · Conclusión proporcionada, con una limitación reconocida"), t("The conclusion claims much more than the data show.", "La conclusión afirma mucho más de lo que los datos muestran."), t("The conclusion fits the data but admits no limitation.", "La conclusión se ajusta a los datos, pero no reconoce ninguna limitación."), t("The conclusion answers the starting question and admits at least one limitation.", "La conclusión responde a la pregunta inicial y reconoce al menos una limitación."), t("It also says what extra data or better design would fix that limitation.", "Señala además qué dato adicional o qué mejora del diseño resolvería esa limitación.")],
         [t("5 · A clear oral presentation, with correct science words", "5 · Presentación oral clara, con lenguaje científico correcto"), t("The parts of the investigation cannot be told apart.", "No se distinguen las partes de la investigación al exponer."), t("Presents the parts but mixes up basic science terms.", "Expone las partes, pero confunde términos científicos básicos."), t("Presents the six stages clearly and uses the right words.", "Presenta las seis etapas con claridad y emplea el vocabulario correcto."), t("Also answers the listener’s questions using their own data.", "Responde además las preguntas de quien lo escucha, apoyándose en sus propios datos.")]])
    banco = C.tabla(t("Twenty questions you can investigate at home, by area", "Banco de veinte preguntas investigables factibles en casa, agrupadas por ámbito"),
        [t("Area", "Ámbito"), t("Possible questions", "Preguntas posibles")],
        [[t("Heat and temperature", "Calor y temperatura"), t("Does coffee cool faster in a ceramic mug or a metal one? · Does a lid change how fast it cools? · How long does an ice cube take to melt in different liquids? · Does a dark surface or a light one get hotter in the sun?", "¿Se enfría el café más rápido en taza de cerámica o de metal? · ¿Influye la tapa en la velocidad de enfriamiento? · ¿Cuánto tarda en derretirse un cubito según el líquido en que se sumerja? · ¿Se calienta más una superficie oscura o una clara al sol?")],
         [t("Plants and sprouting", "Plantas y germinación"), t("Do seeds sprout faster with light or without it? · Does the amount of water change a plant’s height? · Does a plant grow the same with tap water and with boiled, cooled water? · Does planting depth matter?", "¿Germinan las semillas más rápido con luz o sin ella? · ¿Influye la cantidad de agua en la altura de la planta? · ¿Crece igual una planta regada con agua del grifo que con agua hervida y enfriada? · ¿Afecta la profundidad a la que se siembra la semilla?")],
         [t("Dissolving and materials", "Disoluciones y materiales"), t("Does sugar dissolve faster in cold or hot water? · Does stirring change the dissolving time? · Which material soaks up the most water in one minute? · How many drops of water fit on a coin, by coin size?", "¿Se disuelve el azúcar más rápido en agua fría o caliente? · ¿Influye remover en el tiempo de disolución? · ¿Qué material absorbe más agua en un minuto? · ¿Cuántas gotas de agua caben sobre una moneda según su tamaño?")],
         [t("Motion and force", "Movimiento y fuerza"), t("Does a ball rolled from a higher ramp go farther? · Does the surface change how far an object slides? · Does the shape of a sheet of paper change how long it takes to fall? · How long does a pendulum take to stop, by its length?", "¿Llega más lejos una pelota lanzada desde una rampa más alta? · ¿Influye la superficie en la distancia que recorre un objeto al deslizarse? · ¿Cambia el tiempo de caída según la forma del papel? · ¿Cuánto tarda un péndulo en detenerse según su longitud?")],
         [t("Everyday life", "Vida cotidiana y entorno"), t("Which appliance at home uses the most electricity in an hour? · Does the temperature change between rooms during the day? · How much water is used brushing your teeth with the faucet on versus off? · Does street noise change with the time of day?", "¿Qué aparato de la casa consume más electricidad en una hora? · ¿Varía la temperatura entre habitaciones a lo largo del día? · ¿Cuánta agua se gasta al lavarse los dientes con el grifo abierto frente a cerrado? · ¿Cambia el nivel de ruido de la calle según la hora?")]])
    filas_datos = "\n".join(
        f'<tr><th scope="row">{i}</th>'
        f'<td><input type="text" id="d{i}-c" data-campo="d{i}-c" aria-label="{t("Trial", "Medición")} {i}: {t("condition tested", "condición ensayada")}"></td>'
        f'<td><input type="text" inputmode="decimal" id="d{i}-v" data-campo="d{i}-v" aria-label="{t("Trial", "Medición")} {i}: {t("value measured", "valor medido")}"></td>'
        f'<td><input type="text" id="d{i}-u" data-campo="d{i}-u" aria-label="{t("Trial", "Medición")} {i}: {t("unit", "unidad")}"></td>'
        f'<td><input type="text" id="d{i}-o" data-campo="d{i}-o" aria-label="{t("Trial", "Medición")} {i}: {t("notes", "observaciones")}"></td></tr>' for i in range(1, 13))

    e1 = (f'<p>{t("Write the question you will investigate. It must be something you can answer by measuring.", "Escriba la pregunta que va a investigar. Debe poder responderse midiendo algo.")}</p>'
          f'<div class="campo"><label for="nombre">{t("Name and start date", "Nombre y fecha de inicio")}</label><input type="text" id="nombre" data-campo="nombre" class="corto"></div>'
          + campo("pregunta", t("My question to investigate", "Mi pregunta investigable"), t("Write it as a full question. Example: “Does coffee cool faster in a ceramic mug than in a metal one?”", "Formúlela como pregunta completa. Ejemplo: «¿Se enfría el café más rápido en una taza de cerámica que en una de metal?»"), 2)
          + campo("interes", t("Why it interests me and what I already know", "Por qué me interesa y qué sé ya sobre el tema"), t("Two or three lines. If something from the course relates to your question, mention it.", "Dos o tres líneas. Si algo de lo estudiado en el curso se relaciona con su pregunta, menciónelo."), 3))
    e2 = (f'<p>{t("A hypothesis <strong>predicts a specific result</strong> and could turn out to be false. “I’ll see what happens” is not a hypothesis; “coffee will cool faster in the metal mug” is.", "Una hipótesis <strong>anticipa un resultado concreto</strong> y puede resultar falsa. «Veré qué pasa» no es una hipótesis; «el café se enfriará más rápido en la taza de metal» sí lo es.")}</p>'
          + C.caja("tip", t("The formula that helps", "La fórmula que ayuda"), "<p>" + t("“<strong>If</strong> [I change this], <strong>then</strong> [this other thing will happen], <strong>because</strong> [reason].” The “because” part is what makes a hypothesis more than a simple guess.", "«<strong>Si</strong> [cambio esto], <strong>entonces</strong> [ocurrirá esto otro], <strong>porque</strong> [razón]». La parte del «porque» es la que distingue una hipótesis de una simple predicción.") + "</p>")
          + campo("hipotesis", t("My hypothesis", "Mi hipótesis"), "", 3) + campo("base", t("What I base it on", "En qué me baso para pensarlo"), "", 3))
    e3 = (f'<p>{t("Here you decide what you change, what you measure, and what you keep the same. It counts the most in the rubric, and it ruins the most projects when it is rushed.", "Aquí se decide qué se cambia, qué se mide y qué se mantiene igual. Es la parte que más se juega en la rúbrica y la que más proyectos arruina cuando se hace deprisa.")}</p>'
          + campo("vi", t("Independent variable · what I change", "Variable independiente · lo que yo cambio"), t("Only one. Example: the material of the mug.", "Solo una. Ejemplo: el material de la taza."), 2)
          + campo("vd", t("Dependent variable · what I measure", "Variable dependiente · lo que yo mido"), t("Also say with what tool and in what unit. Example: temperature, with a thermometer, in degrees Celsius or Fahrenheit.", "Indique también con qué instrumento y en qué unidad. Ejemplo: la temperatura, con termómetro, en grados Celsius."), 2)
          + campo("constantes", t("What I keep the same", "Lo que mantengo constante"), t("Everything else. Example: the same amount of liquid, the same starting temperature, the same place, the same time of day.", "Todo lo demás. Ejemplo: la misma cantidad de líquido, la misma temperatura inicial, el mismo lugar, la misma hora."), 3)
          + campo("control", t("My control group or my repeated trials", "Mi grupo de control o mis repeticiones"), t("What do you compare with? How many times do you repeat each measurement? Repeating at least three times reduces the effect of a one-time error.", "¿Con qué compara? ¿Cuántas veces repite cada medición? Repetir al menos tres veces reduce el efecto de un error puntual."), 3)
          + campo("procedimiento", t("Step-by-step procedure", "Procedimiento paso a paso"), t("Write it so that someone else could repeat it exactly without asking you anything.", "Escríbalo de manera que otra persona pueda repetirlo exactamente igual sin preguntarle nada."), 6)
          + C.caja("ojo", t("Safety first", "Seguridad primero"), "<p>" + t("No project in this course needs dangerous substances, fire without supervision, household electrical wiring, or animals. If your design seems to need any of those, change it before you go on.", "Ningún proyecto de este curso requiere sustancias peligrosas, fuego sin supervisión, electricidad de la red ni animales. Si su diseño parece necesitar algo de eso, cámbielo antes de continuar.") + "</p>"))
    e4 = (f'<p>{t("Write down each measurement <strong>as you take it</strong>, not from memory at the end. If a value looks odd, do not erase it: write it down and comment on it later. Write the condition the same way every time (for example, always “metal” and “ceramic”), so the page can group your trials.", "Anote las mediciones <strong>según las obtiene</strong>, no de memoria al final. Si un dato sale raro, no lo borre: anótelo y coméntelo después. Escriba la condición siempre igual (por ejemplo, siempre «metal» y «cerámica»), para que la página pueda agrupar sus mediciones.")}</p>'
          f'<div aria-label="{t("Data table (you can scroll sideways)", "Tabla de datos (desplazable horizontalmente)")}" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad tabla-datos"><caption class="cap-oculto">{t("Table to record up to twelve measurements: trial number, condition tested, value measured, unit, and notes", "Tabla para registrar hasta doce mediciones: número, condición ensayada, valor medido, unidad y observaciones")}</caption>'
          f'<thead><tr><th scope="col">{t("No.", "N.º")}</th><th scope="col">{t("Condition tested", "Condición ensayada")}</th><th scope="col">{t("Value measured", "Valor medido")}</th><th scope="col">{t("Unit", "Unidad")}</th><th scope="col">{t("Notes", "Observaciones")}</th></tr></thead><tbody>{filas_datos}</tbody></table></div>'
          f'<p class="aviso-desliza"><span aria-hidden="true">↔</span> {t("Slide the table sideways to see all the columns.", "Deslice la tabla horizontalmente para ver todas las columnas.")}</p>'
          f'<p><button class="btn btn-sec" type="button" id="b-resumen">{t("Summarize my data", "Resumir mis datos")}</button></p>'
          f'<div id="resumen" aria-live="polite"></div>'
          + C.caja("tip", t("Which graph?", "¿Qué gráfica?"), "<p>" + t("Choose by your data: <strong>bars</strong> to compare different categories (metal mug versus ceramic); <strong>lines</strong> to follow a change over time; <strong>circle (pie)</strong> only for parts of a whole. The summary above draws a bar graph of the averages to help you check; your own graph, by hand or with a spreadsheet, needs labeled axes and units.", "Elija según sus datos: <strong>barras</strong> para comparar categorías distintas (taza de metal frente a cerámica); <strong>líneas</strong> para seguir un cambio a lo largo del tiempo; <strong>circular</strong> solo para partes de un total. El resumen de arriba dibuja una gráfica de barras de las medias para ayudarle a revisar; su propia gráfica, hecha a mano o con hoja de cálculo, debe llevar los ejes rotulados y las unidades.") + "</p>")
          + campo("grafica", t("Which graph I will make and why", "Qué gráfica voy a hacer y por qué"), "", 3))
    e5 = (f'<p>{t("Answer your starting question with <strong>what your data show</strong>, no more and no less. It is exactly the rule of Lesson 8.1, applied to your own work.", "Responda a su pregunta inicial <strong>con lo que sus datos muestran</strong>, ni más ni menos. Es exactamente el criterio de la Lección 8.1 aplicado a su propio trabajo.")}</p>'
          + campo("conclusion", t("My conclusion", "Mi conclusión"), t("Start by answering the question, and right away cite the data point behind it. Example: “Coffee cooled faster in metal: it dropped 32 °F (18 °C) against 20 °F (11 °C) in the same time.”", "Empiece respondiendo a la pregunta y cite enseguida el dato que lo sostiene. Ejemplo: «El café se enfrió más rápido en metal: bajó 18 °C frente a 11 °C en el mismo tiempo»."), 4)
          + campo("confirmada", t("Was my hypothesis confirmed?", "¿Se confirmó mi hipótesis?"), t("If not, say so clearly. A hypothesis disproved with honest data is worth as much as a confirmed one; what the rubric penalizes is forcing the data to fit.", "Si no se confirmó, dígalo con claridad. Una hipótesis refutada con datos honestos vale igual que una confirmada; lo que la rúbrica penaliza es forzar los datos para que encajen."), 3)
          + campo("limitacion", t("One limitation of my investigation", "Una limitación de mi investigación"), t("Required, and it earns points. Example: I measured on only one day, or I used one thermometer without checking it, or I did three trials and more might be needed.", "Obligatorio, y suma puntos. Ejemplo: solo medí un día, o usé un solo termómetro sin comprobar su precisión, o hice tres repeticiones y quizá hagan falta más."), 3)
          + campo("despues", t("What I would do differently or measure next", "Qué haría distinto o qué mediría después"), "", 3))
    e6 = (f'<p>{t("Five minutes, following the order of the stages, in front of a family member, a friend, or your phone’s camera. Then ask the person listening to ask you two questions. Prepare your script here.", "Cinco minutos, siguiendo el orden de las etapas, ante un familiar, una amistad o la cámara de su teléfono. Después pida a quien lo escuche que le haga dos preguntas. Prepare aquí el guion.")}</p>'
          + campo("guion", t("My presentation script", "Guion de mi presentación"), t("One or two sentences per stage: question, hypothesis, design, data, graph, conclusion. Do not read the whole report: tell what matters.", "Una o dos frases por etapa: pregunta, hipótesis, diseño, datos, gráfica, conclusión. No lea el informe entero: cuente lo esencial."), 6)
          + campo("preguntas", t("Two questions I expect, and my answers", "Dos preguntas que creo que me harán, y mis respuestas"), t("Expecting them is the best preparation. Your answers should rest on your data.", "Anticiparlas es la mejor preparación. La respuesta debe apoyarse en sus datos."), 5))

    etapas = [("e1", t("Stage 1 · The question", "Etapa 1 · La pregunta"), e1), ("e2", t("Stage 2 · The hypothesis", "Etapa 2 · La hipótesis"), e2), ("e3", t("Stage 3 · The design", "Etapa 3 · El diseño"), e3),
              ("e4", t("Stage 4 · The data", "Etapa 4 · Los datos"), e4), ("e5", t("Stage 5 · The conclusion", "Etapa 5 · La conclusión"), e5), ("e6", t("Stage 6 · The presentation", "Etapa 6 · La presentación"), e6)]
    cuerpo_etapas = "\n".join(etapa(i + 1, sid, tit, c) for i, (sid, tit, c) in enumerate(etapas))
    idx = "".join(f'<li><a href="#{s}">{x}</a></li>' for s, x in [("s-plantilla", t("How to use this workbook", "Cómo trabajar con esta plantilla")), ("s-rubrica", t("The rubric, from day one", "La rúbrica, desde el primer día")), ("s-elegir", t("Choosing the question", "Elegir la pregunta"))] + [(s, x) for s, x, _ in etapas] + [("s-vocab", t("Project vocabulary", "Vocabulario del proyecto")), ("s-evaluar", t("How to grade it", "Cómo evaluarlo")), ("s-sigue", t("Coming next", "Lo que viene"))])
    titulos = {sid: tit for sid, tit, _ in etapas}
    etiquetas = {}
    for m in re.finditer(r'<label for="([^"]+)">([^<]+)</label>', "".join(c for _, _, c in etapas)):
        etiquetas[m.group(1)] = m.group(2)
    orden = [("e1", ["nombre", "pregunta", "interes"]), ("e2", ["hipotesis", "base"]), ("e3", ["vi", "vd", "constantes", "control", "procedimiento"]), ("e4", ["DATOS", "grafica"]), ("e5", ["conclusion", "confirmada", "limitacion", "despues"]), ("e6", ["guion", "preguntas"])]
    info = {"clave": "learnged-ciencias-proyecto-" + L, "orden": [[titulos[s], [[f, etiquetas.get(f, "")] for f in fs]] for s, fs in orden],
            "txt": {"guardado": t("Draft saved in this browser at ", "Borrador guardado en este navegador a las "), "cargado": t("Your saved draft was loaded.", "Se cargó su borrador guardado."),
                    "borrar": t("Press again within 5 seconds to erase everything. This cannot be undone.", "Pulse otra vez en menos de 5 segundos para borrar todo. No se puede deshacer."), "borrado": t("Everything was erased.", "Se borró todo."),
                    "sin": t("(not filled in)", "(sin completar)"), "datos": t("Data", "Datos"), "media": t("average", "media"), "n": t("trials", "mediciones"), "cond": t("Condition", "Condición"), "ncab": t("Trials", "Mediciones"), "mcab": t("Average", "Media"),
                    "nodatos": t("Type at least one condition with a numeric value to see the summary.", "Escriba al menos una condición con un valor numérico para ver el resumen."),
                    "resumen": t("Summary of your data: average of each condition.", "Resumen de sus datos: media de cada condición."),
                    "aviso1": t("Only one trial for: ", "Solo una medición en: "), "aviso2": t(". Repeat at least three times.", ". Repita al menos tres veces."),
                    "graf": t("Bar graph of the average of each condition", "Gráfica de barras de la media de cada condición"), "titulo": t("FINAL PROJECT · MY OWN INVESTIGATION", "PROYECTO FINAL · MI PROPIA INVESTIGACIÓN"),
                    "copiado": t("Report copied. You can paste it into an email or a document.", "Informe copiado. Puede pegarlo en un correo o en un documento."), "nocopia": t("Select the text and copy it with Ctrl+C (Cmd+C on a Mac).", "Seleccione el texto y cópielo con Ctrl+C (Cmd+C en Mac).")}}
    logica = r'''
var INFO = window.INFO, X = INFO.txt;
function $(id){ return document.getElementById(id); }
function campos(){ return [].slice.call(document.querySelectorAll("[data-campo]")); }
function lee(){ var o = {}; campos().forEach(function(c){ o[c.dataset.campo] = c.value; }); return o; }
function escribe(o){ campos().forEach(function(c){ if (o[c.dataset.campo] != null) c.value = o[c.dataset.campo]; }); }
function aviso(m){ $("estado").textContent = m; }
function guarda(silencio){ try { localStorage.setItem(INFO.clave, JSON.stringify(lee())); if (!silencio){ var d = new Date(); aviso(X.guardado + d.toLocaleTimeString()); } } catch(e){} }
function num(s){ s = String(s || "").trim().replace(/\s/g, ""); if (!s) return null; if (/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(s)) s = s.replace(/,/g, ""); else s = s.replace(",", "."); var v = Number(s); return isFinite(v) ? v : null; }
function filas(){ var out = []; for (var i = 1; i <= 12; i++){ var c = $("d" + i + "-c").value.trim(), v = $("d" + i + "-v").value.trim(), u = $("d" + i + "-u").value.trim(), o = $("d" + i + "-o").value.trim(); if (c || v || u || o) out.push({i: i, c: c, v: v, u: u, o: o}); } return out; }
function grupos(){ var g = {}, ord = []; filas().forEach(function(f){ var v = num(f.v); if (!f.c || v === null) return; var k = f.c.toLowerCase(); if (!g[k]){ g[k] = {nom: f.c, vals: [], u: f.u}; ord.push(k); } g[k].vals.push(v); if (!g[k].u && f.u) g[k].u = f.u; }); return ord.map(function(k){ var x = g[k]; x.media = x.vals.reduce(function(a, b){ return a + b; }, 0) / x.vals.length; return x; }); }
function fmt(v){ return (Math.round(v * 100) / 100).toLocaleString("en-US"); }
function esc(s){ return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function resumen(){
  var gs = grupos(), r = $("resumen");
  if (!gs.length){ r.innerHTML = "<p>" + X.nodatos + "</p>"; return; }
  var una = gs.filter(function(g){ return g.vals.length < 2; }).map(function(g){ return esc(g.nom); });
  var h = "<p><strong>" + X.resumen + "</strong></p><table class=\"tabla-trad\"><caption class=\"cap-oculto\">" + X.resumen + "</caption><thead><tr><th scope=\"col\">" + X.cond + "</th><th scope=\"col\">" + X.ncab + "</th><th scope=\"col\">" + X.mcab + "</th></tr></thead><tbody>" +
    gs.map(function(g){ return "<tr><th scope=\"row\">" + esc(g.nom) + "</th><td>" + g.vals.length + "</td><td>" + fmt(g.media) + (g.u ? " " + esc(g.u) : "") + "</td></tr>"; }).join("") + "</tbody></table>";
  var mx = Math.max.apply(null, gs.map(function(g){ return g.media; })), mn = Math.min(0, Math.min.apply(null, gs.map(function(g){ return g.media; })));
  var W = 520, H = 260, x0 = 60, y0 = 20, ah = 180, bw = Math.min(90, (W - x0 - 20) / gs.length - 20), rango = (mx - mn) || 1;
  var y = function(v){ return y0 + ah - (v - mn) / rango * ah; };
  var s = "<svg viewBox=\"0 0 " + W + " " + H + "\" style=\"width:100%;max-width:" + W + "px;height:auto\" role=\"img\" aria-label=\"" + X.graf + ": " + gs.map(function(g){ return esc(g.nom) + " " + fmt(g.media); }).join(", ") + "\">";
  s += "<line x1=\"" + x0 + "\" y1=\"" + y(mn) + "\" x2=\"" + (W - 10) + "\" y2=\"" + y(mn) + "\" stroke=\"#222\" stroke-width=\"2\"/><line x1=\"" + x0 + "\" y1=\"" + y0 + "\" x2=\"" + x0 + "\" y2=\"" + (y0 + ah) + "\" stroke=\"#222\" stroke-width=\"2\"/>";
  gs.forEach(function(g, k){ var bx = x0 + 20 + k * (bw + 20), top = y(Math.max(g.media, 0)), bot = y(Math.min(g.media, 0));
    s += "<rect x=\"" + bx + "\" y=\"" + top + "\" width=\"" + bw + "\" height=\"" + Math.max(bot - top, 1) + "\" fill=\"#5b8def\" stroke=\"#1e3a8a\"/>";
    s += "<text x=\"" + (bx + bw / 2) + "\" y=\"" + (top - 6) + "\" font-size=\"13\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#1e3a8a\">" + fmt(g.media) + "</text>";
    s += "<text x=\"" + (bx + bw / 2) + "\" y=\"" + (y0 + ah + 20) + "\" font-size=\"13\" text-anchor=\"middle\" fill=\"#222\">" + esc(g.nom.length > 14 ? g.nom.slice(0, 13) + "…" : g.nom) + "</text>"; });
  s += "<text x=\"16\" y=\"" + (y0 + ah / 2) + "\" font-size=\"12\" text-anchor=\"middle\" fill=\"#222\" transform=\"rotate(-90 16 " + (y0 + ah / 2) + ")\">" + X.mcab + (gs[0].u ? " (" + esc(gs[0].u) + ")" : "") + "</text></svg>";
  h += s;
  if (una.length) h += "<p class=\"aviso-corto\">" + X.aviso1 + una.join(", ") + X.aviso2 + "</p>";
  r.innerHTML = h;
}
function informe(){
  var o = lee(), L = [X.titulo, ""];
  INFO.orden.forEach(function(e){
    L.push("== " + e[0].toUpperCase() + " ==");
    e[1].forEach(function(p){
      if (p[0] === "DATOS"){ L.push(X.datos + ":"); var fs = filas(); if (!fs.length) L.push("  " + X.sin); fs.forEach(function(f){ L.push("  " + f.i + ". " + [f.c, f.v + (f.u ? " " + f.u : ""), f.o].filter(Boolean).join(" · ")); });
        var gs = grupos(); if (gs.length){ L.push("  " + X.resumen); gs.forEach(function(g){ L.push("  - " + g.nom + ": " + X.media + " " + fmt(g.media) + (g.u ? " " + g.u : "") + " (" + g.vals.length + " " + X.n + ")"); }); }
        return; }
      L.push(p[1] + ":"); L.push((o[p[0]] || "").trim() || X.sin); L.push("");
    });
    L.push("");
  });
  $("informe-txt").value = L.join("\n"); $("informe-caja").hidden = false; $("informe-txt").focus();
}
$("b-guardar").addEventListener("click", function(){ guarda(false); });
$("b-informe").addEventListener("click", function(){ guarda(true); informe(); });
$("b-copiar").addEventListener("click", function(){ var tx = $("informe-txt"); tx.select(); var ok = false; try { ok = document.execCommand("copy"); } catch(e){} if (navigator.clipboard){ navigator.clipboard.writeText(tx.value).then(function(){ aviso(X.copiado); }, function(){ aviso(X.nocopia); }); } else aviso(ok ? X.copiado : X.nocopia); });
$("b-imprimir").addEventListener("click", function(){ guarda(true); resumen(); window.print(); });
$("b-resumen").addEventListener("click", resumen);
var armado = 0;
$("b-borrar").addEventListener("click", function(){ var ahora = Date.now(); if (ahora - armado > 5000){ armado = ahora; aviso(X.borrar); return; } armado = 0; try { localStorage.removeItem(INFO.clave); } catch(e){} campos().forEach(function(c){ c.value = ""; }); $("resumen").innerHTML = ""; $("informe-caja").hidden = true; aviso(X.borrado); });
var t0; document.addEventListener("input", function(){ clearTimeout(t0); t0 = setTimeout(function(){ guarda(true); }, 1500); });
try { var g = localStorage.getItem(INFO.clave); if (g){ escribe(JSON.parse(g)); aviso(X.cargado); if (grupos().length) resumen(); } } catch(e){}
'''
    estilo = """
  [hidden]{display:none !important;}
  .campo{margin:14px 0;}
  .campo label{display:block;font-weight:700;color:var(--azul-osc,#14265e);margin-bottom:4px;font-size:17px;}
  .campo .ayuda{margin:0 0 6px;font-size:15px;color:#4a5568;}
  textarea.trabajo,input.corto{width:100%;font:inherit;font-size:17px;padding:10px;border:2px solid #b0bec5;border-radius:8px;background:#fff;box-sizing:border-box;}
  input.corto{max-width:520px;}
  textarea.trabajo:focus,input.corto:focus,.tabla-datos input:focus{outline:3px solid #1e3a8a;outline-offset:1px;border-color:#1e3a8a;}
  .tabla-datos input{width:100%;min-width:110px;font:inherit;font-size:16px;padding:6px 8px;border:1px solid #b0bec5;border-radius:6px;box-sizing:border-box;}
  .tabla-datos td{padding:6px !important;}
  .fila-botones{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;}
  #estado{font-weight:600;color:#14265e;min-height:1.4em;}
  #informe-txt{width:100%;min-height:320px;font-family:Consolas,'Courier New',monospace;font-size:14px;padding:10px;border:2px solid #b0bec5;border-radius:8px;box-sizing:border-box;}
  .aviso-corto{background:#fdf3df;border-left:4px solid #5C3900;padding:8px 12px;border-radius:5px;color:#5C3900;font-weight:600;}
  section.etapa{border-top:3px solid #e6e9f2;padding-top:6px;}
  @media print{
    .lg-bar,.saltar,.fila-botones,#informe-caja,.indice,.aviso-desliza,#estado{display:none !important;}
    textarea.trabajo{border:1px solid #000;min-height:0;height:auto;}
    section.etapa{break-inside:auto;}
    body{background:#fff;}
  }"""
    otro = "es" if L == "en" else "en"
    return f'''<!DOCTYPE html>
<!-- LearnGED · {t("Science · Lesson 8.2 · Final project workbook", "Ciencias · Lección 8.2 · Cuaderno del proyecto final")} — {t("built by", "construida con")} tools/build_sci_8_2.py
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{t("Lesson 8.2 · Final project: my own investigation · LearnGED", "Lección 8.2 · Proyecto final: mi propia investigación · LearnGED")}</title>
<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="alternate" hreflang="{otro}" href="/{C.carpeta(otro)}/{C.lec(N, otro)}"/>
<link rel="stylesheet" href="/math/lesson.css">
<link rel="stylesheet" href="/science/science.css">
<style>{estilo}
</style>
</head>
<body data-area="ged">
{C.barra()}
<a class="saltar" href="#indice">{t("Skip to the workbook contents", "Saltar al contenido del cuaderno")}</a>
<header class="principal">
<div class="envoltura-header">
<p class="ruta">{t("Science · Topic", "Ciencias · Tema")} {tn} — {C.tema(tn)}</p>
<h1>{t("Lesson 8.2 · Final project: my own investigation", "Lección 8.2 · Proyecto final: mi propia investigación")}</h1>
<p class="lema">{t("Design a small investigation about something around you, collect your own data, and defend a conclusion that fits them.", "Diseñe una investigación sencilla sobre algo de su entorno, recoja sus propios datos y defienda una conclusión que se ajuste a ellos.")}</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> {t("About 4 hours, spread over two or three weeks", "Unas 4 horas, repartidas en dos o tres semanas")}</span>
<span class="chip chip-sp">SP.1 – SP.8 · {t("All the practices of the course", "Todas las prácticas del curso")}</span>
<span class="chip chip-sp">{t("No quiz · the project is the assessment", "Sin quiz · el proyecto sustituye la evaluación")}</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>{t("What you will do", "Lo que va a hacer")}</h2>
<ul>
<li>{t("<strong>Design</strong> a simple investigation about something in your own surroundings.", "<strong>Diseñar</strong> una investigación sencilla sobre un fenómeno del propio entorno.")}</li>
<li>{t("<strong>Write</strong> a question you can investigate and a hypothesis you can test.", "<strong>Formular</strong> una pregunta investigable y una hipótesis comprobable.")}</li>
<li>{t("<strong>Name</strong> the variables and set up a fair control.", "<strong>Identificar</strong> las variables y establecer un control adecuado.")}</li>
<li>{t("<strong>Collect</strong> your own data, organize them in a table, and show them in the right kind of graph.", "<strong>Recoger</strong> datos propios, organizarlos en una tabla y representarlos en la gráfica apropiada.")}</li>
<li>{t("<strong>Write</strong> a conclusion that fits the data and admits at least one limitation.", "<strong>Formular</strong> una conclusión proporcionada a los datos, reconociendo al menos una limitación.")}</li>
<li>{t("<strong>Present</strong> your investigation out loud, using correct science words.", "<strong>Presentar</strong> oralmente la investigación con lenguaje científico correcto.")}</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">{t("Workbook contents", "Contenido del cuaderno")}</h2><ol>{idx}</ol></nav>

<div class="caja caja-tip"><span class="etiqueta et-verde">{t("Before you start", "Antes de empezar")}</span>
<p>{t("<strong>This page is your workbook.</strong> It is not a lesson to read: it is a template you fill in over about three weeks. Each stage has its fields, and at the end everything comes together in one report.", "<strong>Esta página es su cuaderno de trabajo.</strong> No es una lección para leer: es una plantilla que se va completando a lo largo de unas tres semanas. Cada etapa tiene sus campos, y al final todo queda reunido en un solo informe.")}</p>
<p>{t("<strong>The calendar.</strong> Start early, because some investigations need several days of observation. A good pace: week one for stages 1 to 3, week two to collect data, and week three for the conclusion and the presentation.", "<strong>El calendario.</strong> Conviene empezar pronto, porque varias investigaciones necesitan días de observación. Un buen ritmo es dedicar la primera semana a las etapas 1 a 3, la segunda a recoger los datos y la tercera a la conclusión y a preparar la presentación.")}</p>
<p>{t("<strong>The circle closes.</strong> Topic 1 taught you to write a testable hypothesis and isolate a variable. Everything below is doing it for real, with your own question and your own data.", "<strong>El círculo se cierra.</strong> El Tema 1 enseñó a formular una hipótesis comprobable y a aislar una variable. Todo lo que sigue es hacerlo de verdad, con un fenómeno propio y datos propios.")}</p>
</div>

<section>
<h2 id="s-plantilla"><span aria-hidden="true" class="num-seccion">💾</span>{t("How to use this workbook", "Cómo trabajar con esta plantilla")}</h2>
<p>{t("Type straight into the fields. The page saves a draft in this browser by itself every few seconds, and you can also press <strong>Save draft</strong>. When you come back to this page on the same device, you will find your work where you left it.", "Escriba directamente en los campos. La página guarda sola un borrador en este navegador cada pocos segundos, y también puede pulsar <strong>Guardar borrador</strong>. Al volver a esta página en el mismo equipo, encontrará su trabajo donde lo dejó.")}</p>
{C.caja("ojo", t("A saved draft is not a backup", "El borrador guardado no es una copia de seguridad"), "<p>" + t("It is only on this device and is lost if the browser’s data are cleared or if you use another device. To keep your work, press <strong>Make the report</strong> and copy the text, or use <strong>Print or save as PDF</strong>.", "Solo está en este equipo y se pierde si se borran los datos del navegador o si se usa otro dispositivo. Para conservar su trabajo, pulse <strong>Generar informe</strong> y copie el texto, o use <strong>Imprimir o guardar en PDF</strong>.") + "</p>")}
<div class="fila-botones">
<button class="btn" type="button" id="b-guardar">{t("Save draft", "Guardar borrador")}</button>
<button class="btn" type="button" id="b-informe">{t("Make the report", "Generar informe")}</button>
<button class="btn btn-sec" type="button" id="b-imprimir">{t("Print or save as PDF", "Imprimir o guardar en PDF")}</button>
<button class="btn btn-sec" type="button" id="b-borrar">{t("Erase everything and start over", "Borrar todo y empezar de nuevo")}</button>
</div>
<p id="estado" role="status" aria-live="polite"></p>
<div id="informe-caja" hidden>
<label for="informe-txt"><strong>{t("Full report, ready to copy", "Informe completo, listo para copiar")}</strong></label>
<textarea id="informe-txt" readonly></textarea>
<p><button class="btn btn-sec" type="button" id="b-copiar">{t("Copy the report", "Copiar el informe")}</button></p>
</div>
</section>

<section>
<h2 id="s-rubrica"><span aria-hidden="true" class="num-seccion">📊</span>{t("The rubric, from day one", "La rúbrica, desde el primer día")}</h2>
<p>{t("This rubric does not appear at the end to grade you: you get it now, at the start, because <strong>it is the guide for the work</strong>. Each criterion says what the project must contain, and the “Advanced” column shows what to aim for. Five criteria, four levels each: up to 20 points.", "Esta rúbrica no aparece al final para calificar: se entrega ahora, al empezar, porque <strong>es la guía del trabajo</strong>. Cada criterio indica qué debe contener el proyecto, y la columna «Destacado» describe adónde conviene apuntar. Cinco criterios con cuatro niveles: hasta 20 puntos.")}</p>
{C.caja("tip", t("Look at criterion 4", "Fíjese en el criterio 4"), "<p>" + t("<strong>Admitting a limitation adds points; it does not take them away.</strong> A project that admits what its data cannot show is better done, not worse.", "<strong>Reconocer una limitación suma puntos, no los resta.</strong> Un proyecto que admite lo que sus datos no permiten afirmar está mejor hecho, no peor.") + "</p>")}
{rub}
</section>

<section>
<h2 id="s-elegir"><span aria-hidden="true" class="num-seccion">❓</span>{t("Choosing the question", "Elegir la pregunta")}</h2>
<p>{t("A <strong>question you can investigate</strong> is one you can answer <strong>by measuring something</strong>. Questions that ask for an opinion (“Is coffee better than tea?”) or that you answer by looking it up (“At what temperature does water boil?”) do not count. The test is simple: if answering it means <strong>doing something and writing down numbers</strong>, you can investigate it.", "Una <strong>pregunta investigable</strong> es la que puede responderse <strong>midiendo algo</strong>. No lo son las que piden una opinión («¿es mejor el café que el té?») ni las que se contestan buscando el dato en un libro («¿a qué temperatura hierve el agua?»). La prueba es sencilla: si para responderla hay que <strong>hacer algo y anotar números</strong>, es investigable.")}</p>
{C.caja("tip", t("Start small", "Empiece por lo pequeño"), "<p>" + t("A good project for this course is done at home, with what you have at home, and changes only one thing. Projects almost never fail for lack of ambition: they fail by trying to measure too many things at once.", "Un buen proyecto de este curso se hace en casa, con lo que hay en casa, y cambia una sola cosa. Los proyectos que fracasan casi nunca fracasan por falta de ambición: fracasan por intentar medir demasiadas cosas a la vez.") + "</p>")}
{banco}
<p>{t("<strong>Any other question is welcome</strong>, as long as it meets three conditions: it is answered by measuring, only one thing changes at a time, and it can be done safely with what you have. If you come up with your own, check with your teacher that it meets all three before you start collecting data.", "<strong>Se admite cualquier otra pregunta</strong>, siempre que cumpla tres condiciones: que se responda midiendo, que solo cambie una cosa cada vez y que pueda hacerse con seguridad y con lo que se tenga a mano. Si se le ocurre una propia, compruebe con su profesor o profesora que cumple las tres condiciones antes de empezar a recoger datos.")}</p>
<p>{t("Complete each stage at its time. Do not write the conclusion before you have the data, and do not start measuring before you decide what stays the same.", "Complete cada etapa en su momento. No conviene adelantar la conclusión antes de tener los datos, ni empezar a medir sin haber decidido qué se mantiene constante.")}</p>
</section>

{cuerpo_etapas}

<section>
<h2 id="s-vocab"><span aria-hidden="true" class="num-seccion">🔤</span>{t("Project vocabulary", "Vocabulario del proyecto")}</h2>
<p>{t(f"<strong>Hypothesis</strong> comes from the Greek {R('hypó-')}, under, and <em>thesis</em>, placing: what is placed underneath as a temporary base, waiting to be checked. <strong>Variable</strong> comes from the Latin <em>variare</em>, to change; the <strong>independent</strong> one changes because the investigator decides it, and the <strong>dependent</strong> one changes in response. <strong>Control</strong>, from the old French <em>contre-rôle</em>, the duplicate record used to check the original: the control group is exactly that second copy you compare with. <strong>Data</strong> comes from {R('datum')}, what is given, and that is its nature: you collect it, you do not decide it. <strong>Conclusion</strong>, from <em>com-</em> and <em>claudere</em>, to close together: what closes the reasoning. <strong>Limitation</strong>, from {R('limes')}, border: marking how far your claim can go.", f"<strong>Hipótesis</strong> procede del griego {R('hypó-')}, debajo, y <em>thesis</em>, colocación: lo que se pone debajo como base provisional, a la espera de comprobarlo. <strong>Variable</strong> viene del latín <em>variare</em>, cambiar; la <strong>independiente</strong> cambia porque el investigador lo decide, y la <strong>dependiente</strong> cambia en respuesta. <strong>Control</strong>, del francés antiguo <em>contre-rôle</em>, el registro duplicado que servía para verificar el original: el grupo de control es justamente esa segunda copia con la que se compara. <strong>Dato</strong> procede de {R('datum')}, lo dado, y esa es su naturaleza: se recoge, no se decide. <strong>Conclusión</strong>, de <em>cum</em> y <em>claudere</em>, cerrar juntamente: lo que cierra el razonamiento. <strong>Limitación</strong>, de {R('limes')}, frontera: señalar hasta dónde llega lo que se puede afirmar.")}</p>
</section>

<section>
<h2 id="s-evaluar"><span aria-hidden="true" class="num-seccion">✅</span>{t("How to grade it", "Cómo evaluarlo")}</h2>
<p>{t("Press <strong>Make the report</strong>, copy the text, and give it to your teacher to grade with the rubric of this project, criterion by criterion. Before you hand it in, grade it yourself with the same rubric, and apply the rule of Lesson 8.1: does every claim in your conclusion rest on a number in your table? Then check your presentation against criterion 5.", "Pulse <strong>Generar informe</strong>, copie el texto y entrégueselo a su profesor o profesora para que lo evalúe con la rúbrica de este proyecto, criterio por criterio. Antes de entregarlo, califíquelo usted con la misma rúbrica y aplíquele el criterio de la Lección 8.1: ¿cada afirmación de su conclusión se apoya en una cifra de su tabla? Después revise su presentación con el criterio 5.")}</p>
</section>

<section class="cierre">
<h2 id="s-sigue"><span aria-hidden="true" class="num-seccion">➡️</span>{t("Coming next", "Lo que viene")}</h2>
<p>{t("The project closes the path that started in Topic 1. That topic taught you to write a testable hypothesis and isolate a variable in other people’s investigations; this project asked you to do it with your own question, your own data, and a conclusion you had to defend with them.", "Con el proyecto se cierra el recorrido que empezó en el Tema 1. Aquel tema enseñó a formular una hipótesis comprobable y a aislar una variable sobre investigaciones ajenas; este proyecto ha exigido hacerlo con un fenómeno propio, datos propios y una conclusión que había que defender con esos datos.")}</p>
<p>{t("Only one lesson is left. Lesson 8.3 does not teach science: it teaches <strong>how to take the test</strong>. The item types on the screen (drag and drop, drop-down menus, fill in the blank, hot spot), managing your time, and a complete timed practice test. Try to arrive with your project finished.", "Queda una sola lección. La 8.3 no enseña ciencia: enseña <strong>a rendir el examen</strong>. Los tipos de pregunta que aparecen en la pantalla (arrastrar y soltar, menús desplegables, completar espacios, punto en una imagen), la administración del tiempo y un simulacro cronometrado completo. Conviene llegar con el proyecto ya terminado.")}</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> {t("Next", "Siguiente")}: <a href="{C.lec("8-3")}">{t("Lesson 8.3 · Timed practice test and item types", "Lección 8.3 · Simulacro cronometrado y tipos de pregunta")}</a></p>
</section>
</div>
<footer><p>LearnGED · {t("Science · Topic 8 · Lesson 8.2", "Ciencias · Tema 8 · Lección 8.2")}</p>{C.PIE[L]}</footer>
<script>
window.INFO = {json.dumps(info, ensure_ascii=False)};
{logica}
</script>
</body>
</html>
'''


if __name__ == "__main__":
    for lang in ("en", "es"):
        C.L = lang
        ruta = os.path.join(C.ROOT, C.carpeta(), C.lec(N))
        open(ruta, "w", encoding="utf-8").write(pagina())
        print("ok", os.path.relpath(ruta, C.ROOT))
    C.L = "en"
