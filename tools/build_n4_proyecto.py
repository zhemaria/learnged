"""Level 4 · Lesson 8.3 · Final project template «My mathematical model» — builds the page in English and in Spanish.
From GEDparaHispanos (clase_mate4/leccion_8-3.html, the project «Mi modelo matemático»), rebuilt for LearnGED:
  math/level-4/project-level-4.html · es/matematicas/nivel-4/proyecto-nivel-4.html
The student describes a real situation and types a quadratic or exponential function and the work; the page draws the graph with its
labels, checks the vertex, the intercepts, or the growth rate and a value at a point, saves everything in this browser (localStorage),
and prints to PDF with every section open."""
import os
import bilingue as B
from bilingue import t
from es.traduce import Traductor
import n4
from build_n4_lesson_8_1 import TEMA, SCRIPTS

B.NIVEL = 4
ROOT = B.ROOT

ESTILO = n4.ESTILO + """
  [hidden]{display:none !important;}
  textarea.trabajo{width:100%;min-height:150px;font:inherit;font-size:17px;padding:10px;border:2px solid #b0bec5;border-radius:8px;}
  .tabla-est{border-collapse:collapse;margin:10px 0;font-size:16px;width:100%;}
  .tabla-est th,.tabla-est td{border:1px solid #c8c8c8;padding:6px 10px;text-align:left;}
  .tabla-est th{background:var(--tema-bg);color:var(--tema-d);}
  .guardado{font-size:14px;color:var(--gris);}
  .lista-cierre label{display:flex;gap:10px;align-items:flex-start;margin:8px 0;}
  .lista-cierre input{margin-top:5px;width:20px;height:20px;}
  .titulo-graf{text-align:center;font-weight:700;margin:6px 0;}
  @media print{
    .lg-bar,.saltar,.fila-btn,.no-imp,#gph-calc-btn,.gph-calc,[data-gph-calculadora],.indice,.volver{display:none !important;}
    details.modulo{break-inside:auto;} textarea.trabajo{border:1px solid #000;min-height:0;}
    body{background:#fff;}
  }"""

LOGICA = r'''
var CLAVE = "learnged-n4-proyecto-" + (ES ? "es" : "en");
function esc(x){ return String(x).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
function num(id){ return leeDecimal(String($(id).value).replace(/,/g, "")); }
function r3(v){ return Math.round(v * 1000) / 1000; }
function nn(v){ var r = r3(v); return (r < 0 ? "−" : "") + Math.abs(r).toLocaleString("en-US", {maximumFractionDigits: 3}); }
function modelo(){ var tipo = $("fn-tipo").value;
  if (tipo === "cuad"){ var a = num("fn-a"), b = num("fn-b"), c = num("fn-c"); if (a === null || b === null || c === null) return null; if (!a) return {error: T("a cannot be 0: without x² the function is not quadratic.", "a no puede ser 0: sin x² la función no es cuadrática.")};
    return {tipo: tipo, a: a, b: b, c: c, f: function(x){ return a * x * x + b * x + c; }, txt: pVis([c, b, a])}; }
  var A = num("fn-a0"), B = num("fn-b0"); if (A === null || B === null) return null; if (B <= 0 || B === 1) return {error: T("The base must be positive and different from 1.", "La base debe ser positiva y distinta de 1.")};
  return {tipo: tipo, a: A, b: B, f: function(x){ return A * Math.pow(B, x); }, txt: nn(A) + " · (" + nn(B) + ")<sup>x</sup>"}; }
function nombreF(){ return ($("fn-nombre").value.trim() || "f") ; }
function pintaFuncion(M){ $("fn-cuad").hidden = $("fn-tipo").value !== "cuad"; $("fn-exp").hidden = $("fn-tipo").value === "cuad";
  $("fn-muestra").innerHTML = !M ? T("Type the numbers of your function.", "Escriba los números de su función.") : M.error ? '<span style="color:#b71c1c">' + M.error + "</span>" : "<strong>" + esc(nombreF()) + "(x) = " + M.txt + "</strong>"; }
function pintaGraf(M){ var x0 = num("gr-x0"), x1 = num("gr-x1"), out = $("gr-svg");
  if (!M || M.error){ out.innerHTML = '<p class="nota">' + T("Type your function in section 2 to see the graph.", "Escriba su función en la sección 2 para ver la gráfica.") + "</p>"; return; }
  if (x0 === null || x1 === null || x1 <= x0){ out.innerHTML = '<p class="nota">' + T("Type where x starts and ends (the end greater than the start).", "Escriba dónde empieza y dónde termina x (el final mayor que el inicio).") + "</p>"; return; }
  x0 = Math.floor(x0); x1 = Math.ceil(x1); var ys = []; for (var i = 0; i <= 60; i++) ys.push(M.f(x0 + (x1 - x0) * i / 60));
  var lo = Math.min(0, Math.min.apply(null, ys)), hi = Math.max(0, Math.max.apply(null, ys)); if (hi - lo < 1){ hi += 1; }
  var R = {x0: Math.min(x0, 0), x1: Math.max(x1, 0), y0: Math.floor(lo - (hi - lo) * .05), y1: Math.ceil(hi + (hi - lo) * .1)};
  var pts = []; if (M.tipo === "cuad"){ var xv = -M.b / (2 * M.a); if (xv >= R.x0 && xv <= R.x1) pts.push([xv, M.f(xv), "#c62828", (M.a < 0 ? T("maximum ", "máximo ") : T("minimum ", "mínimo ")) + "(" + nn(xv) + ", " + nn(M.f(xv)) + ")", 7, M.a < 0, true]); }
  else if (0 >= R.x0 && 0 <= R.x1) pts.push([0, M.a, "#2e7d32", "(0, " + nn(M.a) + ")", 7, true, true]);
  var xp = num("an-x"); if (xp !== null && xp >= R.x0 && xp <= R.x1) pts.push([xp, M.f(xp), "#6a1b9a", "(" + nn(xp) + ", " + nn(M.f(xp)) + ")", 6, M.tipo !== "cuad" || M.a > 0, xp < (R.x0 + R.x1) / 2]);
  var tit = esc($("p-titulo").value.trim() || T("My mathematical model", "Mi modelo matemático")), ex = esc($("gr-ex").value.trim() || "x"), ey = esc($("gr-ey").value.trim() || "y");
  out.innerHTML = '<p class="titulo-graf">' + tit + "</p>" + grafFun({rango: R, curvas: [{f: function(x){ return x >= x0 && x <= x1 ? M.f(x) : NaN; }}], puntos: pts,
    voz: T("Graph of ", "Gráfica de ") + esc(nombreF()) + "(x) = " + M.txt.replace(/<\/?sup>/g, "") + T(" from x = ", " de x = ") + x0 + T(" to x = ", " a x = ") + x1 + ". " + T("Horizontal axis: ", "Eje horizontal: ") + ex + ". " + T("Vertical axis: ", "Eje vertical: ") + ey + "."}) +
    '<p class="nota">' + T("Horizontal axis (x): ", "Eje horizontal (x): ") + "<strong>" + ex + "</strong> · " + T("Vertical axis (y): ", "Eje vertical (y): ") + "<strong>" + ey + "</strong></p>"; }
function pintaAnalisis(M){ var out = $("an-auto");
  if (!M || M.error){ out.innerHTML = '<p class="nota">' + T("The check appears when your function is complete.", "La comprobación aparece cuando su función está completa.") + "</p>"; return; }
  var filas = [];
  if (M.tipo === "cuad"){ var xv = -M.b / (2 * M.a), D = M.b * M.b - 4 * M.a * M.c;
    filas.push([T("Opening", "Apertura"), M.a > 0 ? T("up (a &gt; 0): the vertex is a minimum", "hacia arriba (a &gt; 0): el vértice es un mínimo") : T("down (a &lt; 0): the vertex is a maximum", "hacia abajo (a &lt; 0): el vértice es un máximo")]);
    filas.push([T("Vertex", "Vértice"), "x = −b/(2a) = " + nn(xv) + "; y = " + nn(M.f(xv)) + " → (" + nn(xv) + ", " + nn(M.f(xv)) + ")"]);
    filas.push([T("Axis of symmetry", "Eje de simetría"), "x = " + nn(xv)]);
    filas.push([T("y-intercept", "Intercepto con el eje y"), "(0, " + nn(M.c) + ")"]);
    filas.push([T("x-intercepts", "Interceptos con el eje x"), D < 0 ? T("none (discriminant " + nn(D) + " &lt; 0)", "ninguno (discriminante " + nn(D) + " &lt; 0)") : D === 0 ? "(" + nn(xv) + ", 0)" : (function(){ var r = [(-M.b - Math.sqrt(D)) / (2 * M.a), (-M.b + Math.sqrt(D)) / (2 * M.a)].sort(function(u, v){ return u - v; }); return "(" + nn(r[0]) + ", 0) " + T("and", "y") + " (" + nn(r[1]) + ", 0)"; })()]); }
  else { var pc = (M.b - 1) * 100;
    filas.push([T("Behavior", "Comportamiento"), M.b > 1 ? T("growth (b &gt; 1)", "crecimiento (b &gt; 1)") : T("decay (0 &lt; b &lt; 1)", "decaimiento (0 &lt; b &lt; 1)")]);
    filas.push([T("Starting value", "Valor inicial"), "f(0) = " + nn(M.a)]);
    filas.push([T("Change per period", "Cambio por período"), (pc > 0 ? "+" : "−") + nn(Math.abs(pc)) + " % " + T("(each step multiplies by ", "(cada paso multiplica por ") + nn(M.b) + ")"]);
    filas.push([M.b > 1 ? T("Doubling time", "Tiempo para duplicarse") : T("Half-life", "Vida media"), "≈ " + nn(Math.log(M.b > 1 ? 2 : .5) / Math.log(M.b)) + T(" periods", " períodos")]); }
  var xp = num("an-x"); filas.push([T("Value at your point", "Valor en su punto"), xp === null ? T("type a value of x below", "escriba un valor de x abajo") : esc(nombreF()) + "(" + nn(xp) + ") = " + nn(M.f(xp))]);
  out.innerHTML = '<div class="tabla-scroll"><table class="tabla-est"><caption class="sr-only">' + T("Automatic check of your analysis", "Comprobación automática de su análisis") + "</caption><tbody>" + filas.map(function(f){ return '<tr><th scope="row">' + f[0] + "</th><td>" + f[1] + "</td></tr>"; }).join("") + "</tbody></table></div>"; }
function oraciones(s){ return (String(s).match(/[^.!?¡¿]*[a-záéíóúñü0-9][^.!?]*[.!?]/gi) || []).filter(function(x){ return x.trim().split(/\s+/).length >= 3; }).length; }
var CAMPOS = ["p-nombre", "p-fecha", "p-titulo", "si-texto", "si-por", "fn-tipo", "fn-nombre", "fn-a", "fn-b", "fn-c", "fn-a0", "fn-b0", "gr-x0", "gr-x1", "gr-ex", "gr-ey", "an-x", "an-trabajo", "in-texto"];
function guarda(){
  var e = {cierre: [].map.call(document.querySelectorAll(".lista-cierre input"), function(c){ return c.checked; })};
  CAMPOS.forEach(function(id){ e[id] = $(id).value; });
  try { localStorage.setItem(CLAVE, JSON.stringify(e)); $("guardado").textContent = T("Saved in this browser at ", "Guardado en este navegador a las ") + new Date().toLocaleTimeString(ES ? "es" : "en-US", {hour: "2-digit", minute: "2-digit"}) + "."; }
  catch (err){ $("guardado").textContent = T("This browser cannot save. Export to PDF to keep your work.", "Este navegador no puede guardar. Exporte a PDF para conservar su trabajo."); }
}
function restaura(){ var e = null; try { e = JSON.parse(localStorage.getItem(CLAVE) || "null"); } catch (err){} if (!e) return;
  CAMPOS.forEach(function(id){ if (e[id] !== undefined) $(id).value = e[id]; });
  [].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c, i){ c.checked = !!(e.cierre && e.cierre[i]); }); }
var temporizador = null;
function todo(){ var M = modelo(); pintaFuncion(M); pintaGraf(M); pintaAnalisis(M);
  var k = oraciones($("in-texto").value); $("in-cuenta").textContent = T("Sentences found: ", "Oraciones detectadas: ") + k + (k < 5 ? T(" (write at least 5)", " (escriba al menos 5)") : " ✓");
  clearTimeout(temporizador); temporizador = setTimeout(guarda, 500); }
CAMPOS.forEach(function(id){ $(id).addEventListener("input", todo); $(id).addEventListener("change", todo); });
[].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c){ c.addEventListener("change", guarda); });
$("b-pdf").addEventListener("click", function(){ document.querySelectorAll("details.modulo").forEach(function(x){ x.open = true; }); window.print(); });
window.addEventListener("beforeprint", function(){ document.querySelectorAll("details.modulo").forEach(function(x){ x.open = true; }); });
$("b-borrar").addEventListener("click", function(){ $("b-borrar").hidden = true; $("b-borrar-si").hidden = false; $("b-borrar-no").hidden = false; $("borrar-msg").textContent = T("Erase all your work? This cannot be undone.", "¿Borrar todo su trabajo? No se puede deshacer."); });
$("b-borrar-no").addEventListener("click", function(){ $("b-borrar").hidden = false; $("b-borrar-si").hidden = true; $("b-borrar-no").hidden = true; $("borrar-msg").textContent = ""; });
$("b-borrar-si").addEventListener("click", function(){ try { localStorage.removeItem(CLAVE); } catch (err){} CAMPOS.forEach(function(id){ var x = $(id); if (x.tagName === "SELECT") x.selectedIndex = 0; else x.value = ""; }); [].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c){ c.checked = false; }); $("b-borrar-no").click(); todo(); });
$("b-ejemplo").addEventListener("click", function(){ $("fn-tipo").value = "cuad"; $("fn-nombre").value = "h"; $("fn-a").value = "-16"; $("fn-b").value = "64"; $("fn-c").value = "5"; $("gr-x0").value = "0"; $("gr-x1").value = "4"; $("gr-ex").value = T("time (seconds)", "tiempo (segundos)"); $("gr-ey").value = T("height (feet)", "altura (pies)"); $("an-x").value = "1"; if (!$("p-titulo").value) $("p-titulo").value = T("The height of a ball", "La altura de una pelota"); todo(); });
restaura(); todo();
'''

def pagina():
    def campo(i, et, tipo="text", extra=""):
        return f'<div class="campo" style="flex:1;min-width:220px;"><label for="{i}">{et}</label><input type="{tipo}" id="{i}" autocomplete="off" {extra}></div>'
    def corto(i, et, v=""):
        return f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" class="corto" id="{i}" autocomplete="off" value="{v}"></div>'
    rub = [(t("1. Real situation and reasons", "1. Situación real y justificación"), t("No situation, or one that cannot be modeled.", "No describe una situación o no es modelable."), t("Describes the situation, but does not explain the kind of function.", "Describe la situación, pero no justifica el tipo de función."), t("Describes the situation and explains why it is quadratic or exponential.", "Describe la situación y la justifica como cuadrática o exponencial."), t("A rich situation, with clear reasons for the chosen model.", "Describe una situación rica y justifica con claridad el modelo elegido.")),
           (t("2. Graph with labels", "2. Gráfica con etiquetas"), t("No graph, or a wrong one.", "No presenta gráfica o es incorrecta."), t("A graph with missing labels (axes, scale, or units).", "Grafica, pero faltan etiquetas (ejes, escala o unidades)."), t("A correct graph with axes, scale, units, and the name of the function.", "Gráfica correcta con ejes, escala, unidades y nombre de la función."), t("A precise, complete graph, easy to read.", "Gráfica precisa y completa, fácil de leer e interpretar.")),
           (t("3. Algebraic analysis", "3. Análisis algebraico"), t("No analysis, or serious mistakes.", "No realiza análisis o tiene errores graves."), t("A partial analysis, or with calculation mistakes.", "Análisis parcial o con errores de cálculo."), t("Finds the vertex or the rate and the value at a specific point.", "Halla el vértice o la tasa y el valor en un punto específico."), t("A complete, correct analysis with all the key elements.", "Análisis completo y correcto, con todos los elementos clave.")),
           (t("4. Written interpretation", "4. Interpretación escrita"), t("Does not explain the results.", "No interpreta los resultados."), t("An incomplete explanation, or one with no context.", "Interpreta de forma incompleta o sin contexto."), t("Explains the results clearly in the real situation.", "Interpreta los resultados de forma coherente en el contexto real.")
            , t("A complete, clear explanation, connected with the situation.", "Interpretación completa, clara y conectada con la situación.")),
           (t("5. Oral presentation", "5. Presentación oral"), t("No presentation, or it cannot be understood.", "No presenta o no se entiende."), t("Presents, but with little clarity or vague vocabulary.", "Presenta, pero con poca claridad o vocabulario impreciso."), t("Presents clearly with suitable mathematical vocabulary.", "Presenta de forma clara usando vocabulario matemático apropiado."), t("A confident, precise, convincing presentation.", "Presentación segura, precisa y convincente, con buen dominio del tema."))]
    filas_rub = "".join("<tr><th scope=\"row\">" + r[0] + "</th>" + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in rub)
    cierre = [t("<strong>Complete and saved as a PDF</strong>, with the five parts: situation, function, graph, analysis, and interpretation. It is your proof that you finished Level 4.", "<strong>Proyecto completo y guardado en PDF</strong>, con las cinco partes: situación, función, gráfica, análisis e interpretación. Es su constancia de haber terminado el Nivel 4."),
              t("<strong>Presented out loud</strong> in 3 to 4 minutes, to someone you trust or recording yourself on your phone: the situation, the function and its graph, and what the result means. Ask for questions, or ask them yourself as you watch the video.", "<strong>Presentado en voz alta</strong>, de 3 a 4 minutos, a alguien de confianza o grabándose con el teléfono: la situación, la función y su gráfica, y qué significa el resultado. Pida que le hagan preguntas o hágaselas usted al ver el video."),
              t("<strong>Reviewed the next day</strong> with the rubric below in hand, criterion by criterion, as if the work were someone else's.", "<strong>Revisado al día siguiente</strong> con la rúbrica de abajo en la mano, criterio por criterio, como si el trabajo fuera de otra persona."),
              t("<strong>Level 4 final check taken</strong> in real conditions: in one sitting, timing yourself, with only the calculator and the formula sheet.", "<strong>Evaluación final del Nivel 4 hecha</strong> en condiciones reales: de una sentada, tomando el tiempo, solo con la calculadora y la hoja de fórmulas.")]
    mods = [
     (t("instructions", "instrucciones"), t("Project instructions", "Instrucciones del proyecto"),
      f'''      <p>{t("This project brings together what you learned in Level 4, and it is the last piece of the level. You will model a real situation with a <strong>quadratic or exponential</strong> function and present it completely. It must include five parts:", "Este proyecto reúne lo aprendido en el Nivel 4 y es la última pieza del nivel. Usted modelará una situación real con una función <strong>cuadrática o exponencial</strong> y la presentará de forma completa. Debe incluir cinco partes:")}</p>
      <ol><li>{t("<strong>Real situation:</strong> describe what happens and explain why it is quadratic or exponential.", "<strong>Situación real:</strong> describa el fenómeno y justifique por qué es cuadrático o exponencial.")}</li>
      <li>{t("<strong>The function:</strong> write the function that models the situation.", "<strong>La función:</strong> escriba la función que modela la situación.")}</li>
      <li>{t("<strong>The graph:</strong> with axes, scale, units, and the name of the function.", "<strong>La gráfica:</strong> con ejes, escala, unidades y nombre de la función.")}</li>
      <li>{t("<strong>Algebraic analysis:</strong> the vertex (quadratic) or the growth rate (exponential), and the value at a specific point.", "<strong>Análisis algebraico:</strong> el vértice (cuadrática) o la tasa de crecimiento (exponencial), y el valor en un punto específico.")}</li>
      <li>{t("<strong>Written interpretation:</strong> what the result means in the real situation.", "<strong>Interpretación escrita:</strong> qué significa el resultado en el contexto real.")}</li></ol>
      <p>{t("Ideas: the path of a ball (quadratic), savings with compound interest (exponential), the greatest area of a garden with a fixed fence (quadratic), or the growth of followers on social media (exponential).", "Ideas: la trayectoria de una pelota (cuadrática), el ahorro con interés compuesto (exponencial), el área máxima de un jardín con cerca fija (cuadrática) o el crecimiento de seguidores en una red (exponencial).")}</p>
      <div class="caja-tip">{t("The template draws the graph and checks your analysis, but <strong>you must show your work in writing</strong>: the automatic check is only there to check yours.", "La plantilla dibuja la gráfica y comprueba su análisis, pero <strong>usted debe mostrar su procedimiento por escrito</strong>: la comprobación automática solo sirve para verificar el suyo.")}</div>
      <div class="fila-btn no-imp"><button type="button" class="btn" id="b-pdf">{t("Export as PDF", "Exportar como PDF")}</button><button type="button" class="btn-sec" id="b-ejemplo">{t("Load an example (a ball)", "Cargar un ejemplo (una pelota)")}</button><button type="button" class="btn-sec" id="b-borrar">{t("Erase everything", "Borrar todo")}</button><button type="button" class="btn" id="b-borrar-si" hidden>{t("Yes, erase", "Sí, borrar")}</button><button type="button" class="btn-sec" id="b-borrar-no" hidden>{t("No, keep it", "No, conservar")}</button></div>
      <p class="nota" id="borrar-msg" role="status"></p>
      <p class="guardado" id="guardado" aria-live="polite">{t("Your work is saved only in this browser. To keep it, press “Export as PDF” and choose “Save as PDF” as the destination.", "Su trabajo se guarda solo en este navegador. Para conservarlo, pulse «Exportar como PDF» y elija «Guardar como PDF» como destino.")}</p>'''),
     (t("student", "estudiante"), t("0 · About you and your model", "0 · Datos del estudiante y del modelo"),
      f'''      <div class="campos">{campo("p-nombre", t("Student's name", "Nombre del estudiante"))}{campo("p-fecha", t("Due date", "Fecha de entrega"), "date")}</div>
      <div class="campos">{campo("p-titulo", t("Title of your model (for example, “The height of a ball”)", "Título de su modelo (por ejemplo, «La altura de una pelota»)"))}</div>'''),
     (t("situation", "situacion"), t("1 · Real situation", "1 · Situación real"),
      f'''      <div class="campo"><label for="si-texto">{t("Describe the situation: what changes, what you measure, and in what units", "Describa la situación: qué cambia, qué se mide y en qué unidades")}</label><textarea class="trabajo" id="si-texto" style="min-height:110px"></textarea></div>
      <div class="campo"><label for="si-por">{t("Why is it quadratic or exponential?", "¿Por qué es cuadrática o exponencial?")}</label><textarea class="trabajo" id="si-por" style="min-height:90px"></textarea></div>
      <p class="nota">{t("Quadratic: it goes up and then down (or down and then up), with a highest or lowest point. Exponential: it is multiplied by the same factor every period.", "Cuadrática: sube y luego baja (o al revés), con un punto más alto o más bajo. Exponencial: se multiplica por el mismo factor en cada período.")}</p>'''),
     (t("function", "funcion"), t("2 · The function", "2 · La función"),
      f'''      <div class="campos"><div class="campo"><label for="fn-tipo">{t("Kind of function", "Tipo de función")}</label><select id="fn-tipo"><option value="cuad">{t("Quadratic: f(x) = ax² + bx + c", "Cuadrática: f(x) = ax² + bx + c")}</option><option value="exp">{t("Exponential: f(x) = a · bˣ", "Exponencial: f(x) = a · bˣ")}</option></select></div>
        <div class="campo"><label for="fn-nombre">{t("Name of the function (for example, h, A, V)", "Nombre de la función (por ejemplo, h, A, V)")}</label><input type="text" id="fn-nombre" class="corto" autocomplete="off" maxlength="3" value="f"></div></div>
      <div class="campos" id="fn-cuad">{corto("fn-a", "a =")}{corto("fn-b", "b =")}{corto("fn-c", "c =")}</div>
      <div class="campos" id="fn-exp" hidden>{corto("fn-a0", t("a (starting value) =", "a (valor inicial) ="))}{corto("fn-b0", t("b (base) =", "b (base) ="))}</div>
      <p id="fn-muestra" aria-live="polite"></p>'''),
     (t("graph", "grafica"), t("3 · The graph", "3 · La gráfica"),
      f'''      <p>{t("Choose where x starts and ends, and name the two axes with their units. The graph takes the title of your model.", "Elija dónde empieza y dónde termina x y nombre los dos ejes con sus unidades. La gráfica lleva el título de su modelo.")}</p>
      <div class="campos">{corto("gr-x0", t("x from", "x desde"), "0")}{corto("gr-x1", t("x to", "x hasta"), "10")}</div>
      <div class="campos">{campo("gr-ex", t("Horizontal axis (what x is, with units)", "Eje horizontal (qué es x, con unidades)"))}{campo("gr-ey", t("Vertical axis (what y is, with units)", "Eje vertical (qué es y, con unidades)"))}</div>
      <div id="gr-svg"></div>'''),
     (t("analysis", "analisis"), t("4 · Algebraic analysis", "4 · Análisis algebraico"),
      f'''      <p>{t("Quadratic: find the vertex with x = −b/(2a), the axis of symmetry, and the intercepts. Exponential: the starting value and the percent of change per period. In both: the value at a specific point that matters in your situation.", "Cuadrática: halle el vértice con x = −b/(2a), el eje de simetría y los interceptos. Exponencial: el valor inicial y el porcentaje de cambio por período. En las dos: el valor en un punto específico que importe en su situación.")}</p>
      <div class="campo"><label for="an-trabajo">{t("Your process and results (write here)", "Procedimiento y resultados (escriba aquí)")}</label><textarea class="trabajo" id="an-trabajo"></textarea></div>
      <div class="campos">{corto("an-x", t("Your specific point: x =", "Su punto específico: x ="))}</div>
      <h3>{t("Automatic check", "Comprobación automática")}</h3>
      <div id="an-auto"></div>'''),
     (t("interpretation", "interpretacion"), t("5 · Written interpretation", "5 · Interpretación escrita"),
      f'''      <p>{t("Write at least five complete sentences. The numbers do not speak by themselves: explain what they mean.", "Redacte al menos cinco oraciones completas. Los números no hablan solos: explique qué significan.")}</p>
      <div class="caja-tip"><strong>{t("Writing guide", "Guía de redacción")}</strong><ul>
        <li>{t("What does the vertex (or the growth rate) mean in your situation, with its units?", "¿Qué significa el vértice (o la tasa de crecimiento) en su situación, con sus unidades?")}</li>
        <li>{t("What does the value at your specific point tell you?", "¿Qué le dice el valor en su punto específico?")}</li>
        <li>{t("For which values of x does the model make sense (its domain in real life)?", "¿Para qué valores de x tiene sentido el modelo (su dominio en la vida real)?")}</li>
        <li>{t("End with a conclusion of your own: what did you learn about the situation?", "Cierre con una conclusión propia: ¿qué aprendió sobre la situación?")}</li></ul></div>
      <div class="campo"><label for="in-texto">{t("Your interpretation", "Su interpretación")}</label><textarea class="trabajo" id="in-texto" style="min-height:200px"></textarea></div>
      <p class="nota" id="in-cuenta" aria-live="polite"></p>'''),
     (t("finish", "cierre"), t("✓ How to finish the project", "✓ Cómo cerrar el proyecto"),
      f'''      <p>{t("Check each step as you finish it.", "Marque lo que vaya completando.")}</p>
      <div class="lista-cierre">{"".join(f'<label><input type="checkbox"><span>{c}</span></label>' for c in cierre)}</div>'''),
     (t("rubric", "rubrica"), t("Project rubric", "Rúbrica del proyecto"),
      f'''      <p>{t("Five criteria at four levels (20 points in all). Read them before you start, and come back to them when you finish to grade your own work honestly.", "Cinco criterios en cuatro niveles de desempeño (20 puntos en total). Léalos antes de empezar y vuelva a ellos al terminar, para evaluar su propio trabajo con honestidad.")}</p>
      <div class="tabla-scroll"><table class="tabla-est"><caption class="sr-only">{t("Rubric for the final project, with five criteria and four levels", "Rúbrica del proyecto final, con cinco criterios y cuatro niveles")}</caption>
        <thead><tr><th scope="col">{t("Criterion", "Criterio")}</th><th scope="col">{t("Beginning (1)", "Inicial (1)")}</th><th scope="col">{t("Developing (2)", "En desarrollo (2)")}</th><th scope="col">{t("Proficient (3)", "Competente (3)")}</th><th scope="col">{t("Outstanding (4)", "Destacado (4)")}</th></tr></thead>
        <tbody>{filas_rub}</tbody></table></div>
      <p class="nota">{t("The project grade is combined with the grade on the Level 4 final check (30 questions).", "La nota del proyecto se combina con la de la evaluación final del Nivel 4 (30 preguntas).")}</p>''')]
    meta = t("Your work template for the Level 4 final project. Fill it in, check your work, and save it as a PDF.", "Su plantilla de trabajo para el proyecto final del Nivel 4. Complétela, compruebe su trabajo y guárdela en PDF.")
    return B.pagina_practica("8-3", 8, t(*TEMA), t("Final project: My mathematical model", "Proyecto final: Mi modelo matemático"), meta, mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

def construye():
    html = {}
    for lang in ("en", "es"):
        B.L = lang
        s = pagina()
        s = s.replace(f'<h1>{t("Lesson", "Lección")} 8.3 · {t("Final project: My mathematical model", "Proyecto final: Mi modelo matemático")}</h1>', f'<h1>{t("Final project · My mathematical model", "Proyecto final · Mi modelo matemático")}</h1>')
        s = s.replace(f'<title>{t("Practice · Lesson", "Práctica · Lección")} 8.3 · ', f'<title>{t("Final project", "Proyecto final")} · {t("Lesson", "Lección")} 8.3 · ')
        s = s.replace('<a class="lg-link" href="./">Math · Level 4 lessons</a>', f'<a class="lg-link" href="{t("lesson-8-3", "leccion-8-3")}.html">{t("← Back to Lesson 8.3", "← Volver a la Lección 8.3")}</a>')
        s = s.replace("practice (English) — built by", "final project template (English) — built by")
        html[lang] = s
    B.L = "en"
    ruta_en = "math/level-4/project-level-4.html"
    open(os.path.join(ROOT, ruta_en), "w", encoding="utf-8").write(html["en"]); print("ok", ruta_en)
    tr = Traductor(ruta_en, texto=html["es"], nivel=4); tr.frecuentes()
    tr.cabecera("<!-- LearnGED · Nivel 4 · Lección 8.3 · Proyecto final «Mi modelo matemático» — plantilla (español) — construida con tools/build_n4_proyecto.py\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
    ruta_es = "es/matematicas/nivel-4/proyecto-nivel-4.html"
    tr.guarda(ruta_es)
    s = open(os.path.join(ROOT, ruta_es), encoding="utf-8").read()
    s = s.replace('<a class="lg-logo" href="/">', '<a class="lg-logo" href="/es/">').replace('alt="LearnGED home"', 'alt="Inicio de LearnGED"').replace('href="/" style="margin-left:auto;border:1.5px solid #1E3A5F;border-radius:999px;padding:3px 12px"><span aria-hidden="true">🏠 </span>Home</a>', 'href="/es/" style="margin-left:auto;border:1.5px solid #1E3A5F;border-radius:999px;padding:3px 12px"><span aria-hidden="true">🏠 </span>Inicio</a>')
    open(os.path.join(ROOT, ruta_es), "w", encoding="utf-8").write(s)
    for frase in ["Back to contents", "On this page", "Open all", "Math · Level 4"]:
        if frase in s: print("  ¡OJO! queda en inglés en", ruta_es, ":", frase)

if __name__ == "__main__":
    construye()
