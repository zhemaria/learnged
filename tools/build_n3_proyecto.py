"""Level 3 · Lesson 8.3 · Final project template «My data analysis» — builds the page in English and in Spanish.
Imported from GEDparaHispanos (clase_mate3/leccion_8-3_proyecto.html) and rebuilt for LearnGED:
  math/level-3/project-level-3.html · es/matematicas/nivel-3/proyecto-nivel-3.html
The student types the data and the work; the page checks the statistics, draws the graph, checks the probability,
saves everything in this browser (localStorage), and prints to PDF with every section open."""
import os
import bilingue as B
from bilingue import t
from es.traduce import Traductor
from build_n3_explora_8 import ESTILO8, SCRIPTS

B.NIVEL = 3
ROOT = B.ROOT
TEMA = ("Counting and probability", "Combinatoria y probabilidad")

ESTILO = ESTILO8 + """
  [hidden]{display:none !important;}
  .rejilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:8px;margin:10px 0;}
  .rejilla label{font-size:13px;color:var(--gris);display:block;}
  .rejilla input{width:100%;font-size:17px;padding:6px 8px;}
  textarea.trabajo{width:100%;min-height:150px;font:inherit;font-size:17px;padding:10px;border:2px solid #b0bec5;border-radius:8px;}
  .tabla-est{border-collapse:collapse;margin:10px 0;font-size:16px;width:100%;}
  .tabla-est th,.tabla-est td{border:1px solid #c8c8c8;padding:6px 10px;text-align:left;}
  .tabla-est th{background:var(--tema-bg);color:var(--tema-d);}
  .guardado{font-size:14px;color:var(--gris);}
  .lista-cierre label{display:flex;gap:10px;align-items:flex-start;margin:8px 0;}
  .lista-cierre input{margin-top:5px;width:20px;height:20px;}
  @media print{
    .lg-bar,.saltar,.fila-btn,.no-imp,#gph-calc-btn,.gph-calc,[data-gph-calculadora],.indice,.volver{display:none !important;}
    details.modulo{break-inside:auto;} textarea.trabajo{border:1px solid #000;min-height:0;}
    body{background:#fff;}
  }"""

LOGICA = r'''
var CLAVE = "learnged-n3-proyecto-" + (ES ? "es" : "en"), MIN = 10, MAX = 20;
/* (A) Data grid */
function celda(i, v){
  var d = document.createElement("div");
  d.innerHTML = '<label for="dt-' + i + '">' + T("Value ", "Dato ") + (i + 1) + '</label><input type="text" inputmode="decimal" id="dt-' + i + '" autocomplete="off" value="' + (v === undefined || v === null ? "" : String(v).replace(/"/g, "")) + '">';
  d.querySelector("input").addEventListener("input", todo);
  return d;
}
function pintaRejilla(vals){ var r = $("rejilla"); r.innerHTML = ""; vals.forEach(function(v, i){ r.appendChild(celda(i, v)); }); }
function valoresCrudos(){ return [].map.call(document.querySelectorAll("#rejilla input"), function(x){ return x.value; }); }
function valores(){ return valoresCrudos().map(function(x){ return leeDecimal(String(x).replace(/,/g, "")); }).filter(function(v){ return v !== null; }); }
function aviso(msg){ $("dt-aviso").className = msg ? "caja-aviso visible" : "caja-aviso"; $("dt-aviso").textContent = msg || ""; }
$("dt-mas").addEventListener("click", function(){ var v = valoresCrudos(); if (v.length >= MAX){ aviso(T("The project takes at most " + MAX + " values.", "El proyecto admite un máximo de " + MAX + " datos.")); return; } v.push(""); pintaRejilla(v); aviso(""); todo(); $("dt-" + (v.length - 1)).focus(); });
$("dt-menos").addEventListener("click", function(){ var v = valoresCrudos(); if (v.length <= 1) return; v.pop(); pintaRejilla(v); aviso(""); todo(); });
$("dt-cargar").addEventListener("click", function(){
  var partes = $("dt-pegar").value.split(/[\s;,]+/).map(function(x){ return x.trim(); }).filter(Boolean);
  var nums = partes.map(function(x){ return leeDecimal(x); }).filter(function(v){ return v !== null; });
  if (!nums.length){ aviso(T("No numbers were found in what you pasted.", "No se encontraron números en lo que pegó.")); return; }
  if (nums.length > MAX){ nums = nums.slice(0, MAX); aviso(T("Only the first " + MAX + " values were loaded.", "Solo se cargaron los primeros " + MAX + " datos.")); } else aviso("");
  pintaRejilla(nums); todo();
});
/* (B) Statistics */
function moda(o){ var c = {}, mx = 0; o.forEach(function(v){ c[v] = (c[v] || 0) + 1; mx = Math.max(mx, c[v]); }); if (mx < 2) return T("none (no value repeats)", "no hay (ningún dato se repite)"); return Object.keys(c).filter(function(k){ return c[k] === mx; }).map(function(k){ return nm(+k); }).join(", "); }
function r2_(x){ return nm(Math.round(x * 100) / 100); }
function estadisticos(d){
  if (d.length < 2) return null;
  var c = cinco(d), media = d.reduce(function(s, x){ return s + x; }, 0) / d.length, L = limites(c);
  return {n: d.length, media: media, c: c, iqr: c.q3 - c.q1, rango: c.max - c.min, moda: moda(c.o), L: L};
}
function pintaEst(E, d){
  $("dt-cuenta").textContent = T("Valid values: ", "Datos válidos: ") + d.length + (d.length < MIN ? T(" (the project needs at least " + MIN + ")", " (el proyecto necesita al menos " + MIN + ")") : "");
  $("dt-orden").innerHTML = d.length ? chips(ordena(d)) : "—";
  var u = esc($("p-unidad").value.trim()), un = u ? " " + u : "";
  var f = function(k, v){ return "<td>" + (E ? v : "—") + "</td>"; };
  $("est-tabla").innerHTML = '<caption class="sr-only">' + T("Statistics calculated from your data", "Estadísticos calculados a partir de sus datos") + "</caption><tbody>" +
    "<tr><th scope=\"row\">" + T("Number of values (n)", "Cantidad de datos (n)") + "</th>" + f(0, E && E.n) + "<th scope=\"row\">" + T("Mean", "Media") + "</th>" + f(0, E && r2_(E.media) + un) + "</tr>" +
    "<tr><th scope=\"row\">" + T("Minimum", "Mínimo") + "</th>" + f(0, E && nm(E.c.min) + un) + "<th scope=\"row\">" + T("Maximum", "Máximo") + "</th>" + f(0, E && nm(E.c.max) + un) + "</tr>" +
    "<tr><th scope=\"row\">" + T("First quartile (Q1)", "Primer cuartil (Q1)") + "</th>" + f(0, E && nm(E.c.q1) + un) + "<th scope=\"row\">" + T("Third quartile (Q3)", "Tercer cuartil (Q3)") + "</th>" + f(0, E && nm(E.c.q3) + un) + "</tr>" +
    "<tr><th scope=\"row\">" + T("Median (Q2)", "Mediana (Q2)") + "</th>" + f(0, E && nm(E.c.med) + un) + "<th scope=\"row\">IQR</th>" + f(0, E && nm(E.iqr) + un) + "</tr>" +
    "<tr><th scope=\"row\">" + T("Range (max − min)", "Rango (máx − mín)") + "</th>" + f(0, E && nm(E.rango) + un) + "<th scope=\"row\">" + T("Mode", "Moda") + "</th>" + f(0, E && E.moda) + "</tr></tbody>";
  $("est-lim").innerHTML = E ? T("Outlier limits: Q1 − 1.5 × IQR = ", "Límites para valores atípicos: Q1 − 1.5 × IQR = ") + r2_(E.L.inf) + " · Q3 + 1.5 × IQR = " + r2_(E.L.sup) + ". " +
    (function(){ var at = E.c.o.filter(function(v){ return v < E.L.inf || v > E.L.sup; }); return at.length ? T("Outliers: ", "Valores atípicos: ") + listaN(at) + "." : T("No value is an outlier.", "Ningún dato es atípico."); })() : "";
}
/* (C) Graph */
function esc(x){ return String(x).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
function sugerir(d){ if (d.length < 2) return; var o = ordena(d), r = o[o.length - 1] - o[0] || 1, w = Math.max(1, Math.ceil(r / 5)); var cand = [1, 2, 5, 10, 20, 25, 50, 100, 200, 500, 1000]; for (var i = 0; i < cand.length; i++) if (cand[i] >= w){ w = cand[i]; break; } $("gr-ancho").value = w; $("gr-inicio").value = Math.floor(o[0] / w) * w; }
function pintaGraf(E, d){
  var tipo = $("gr-tipo").value, tit = esc($("p-titulo").value.trim() || T("My data", "Mis datos")), u = esc($("p-unidad").value.trim());
  $("gr-hist").hidden = tipo !== "hist";
  if (!E || d.length < 2){ $("gr-svg").innerHTML = '<p class="nota">' + T("Type at least 2 values to see the graph.", "Escriba al menos 2 datos para ver la gráfica.") + "</p>"; return; }
  if (E.c.min === E.c.max){ $("gr-svg").innerHTML = '<p class="nota">' + T("All the values are equal, so there is no spread to draw.", "Todos los datos son iguales: no hay dispersión que dibujar.") + "</p>"; return; }
  var cab = '<p style="text-align:center;font-weight:700;margin:6px 0;">' + tit + (u ? " (" + u + ")" : "") + "</p>";
  if (tipo === "caja"){
    var at = E.c.o.filter(function(v){ return v < E.L.inf || v > E.L.sup; }), ok = E.c.o.filter(function(v){ return v >= E.L.inf && v <= E.L.sup; });
    $("gr-svg").innerHTML = cab + cajaSVG([{c: E.c, atip: at, bigMin: ok[0], bigMax: ok[ok.length - 1]}], T("Box plot of " + tit + ": minimum ", "Diagrama de caja de " + tit + ": mínimo ") + nm(E.c.min) + ", Q1 " + nm(E.c.q1) + T(", median ", ", mediana ") + nm(E.c.med) + ", Q3 " + nm(E.c.q3) + T(", maximum ", ", máximo ") + nm(E.c.max) + ".", {rotulos: true});
  } else {
    var a0 = leeDecimal($("gr-inicio").value), w = leeDecimal($("gr-ancho").value);
    if (a0 === null || w === null || w <= 0){ $("gr-svg").innerHTML = '<p class="nota">' + T("Type the start of the first interval and a width greater than 0.", "Escriba el inicio del primer intervalo y un ancho mayor que 0.") + "</p>"; return; }
    var cl = [], mx = E.c.max; if (a0 > E.c.min) a0 = Math.floor(E.c.min / w) * w;
    for (var a = a0; a <= mx && cl.length < 30; a += w) cl.push({a: a, b: a + w, f: d.filter(function(v){ return v >= a && v < a + w; }).length});
    $("gr-svg").innerHTML = cab + histSVG(cl, T("Histogram of " + tit + ". ", "Histograma de " + tit + ". ") + cl.map(function(c){ return nm(c.a) + "–" + nm(c.b) + ": " + c.f; }).join("; "), {eje: u || T("Values", "Valores")}) +
      '<p class="nota">' + T("Each interval includes its left end but not its right end.", "Cada intervalo incluye su extremo izquierdo, pero no el derecho.") + "</p>";
  }
}
/* (D) Interpretation */
function oraciones(s){ return (String(s).match(/[^.!?¡¿]*[a-záéíóúñü0-9][^.!?]*[.!?]/gi) || []).filter(function(x){ return x.trim().split(/\s+/).length >= 3; }).length; }
/* (E) Probability */
function pintaProb(d){
  var cond = $("pr-cond").value, v1 = leeDecimal($("pr-v1").value), v2 = leeDecimal($("pr-v2").value), n = d.length;
  $("pr-v2c").hidden = cond !== "entre";
  if (!n || v1 === null || (cond === "entre" && v2 === null)){ $("pr-res").innerHTML = '<div class="linea">' + T("Choose a condition and type the reference value.", "Elija una condición y escriba el valor de referencia.") + "</div>"; return; }
  var f = d.filter(function(x){ return cond === "mayor" ? x > v1 : cond === "mayorIg" ? x >= v1 : cond === "menor" ? x < v1 : cond === "menorIg" ? x <= v1 : cond === "igual" ? x === v1 : (x >= Math.min(v1, v2) && x <= Math.max(v1, v2)); }).length;
  var h = '<div class="linea">' + T("Favorable cases: ", "Casos favorables: ") + f + T(" of ", " de ") + n + " → P = " + (f === 0 ? "0" : f === n ? "1" : tresFormas(f, n)) + "</div>";
  if (n >= 2) h += '<div class="linea">' + T("Choosing two values at random, both favorable: with replacement ", "Al elegir dos datos al azar, los dos favorables: con reemplazo ") + (f ? tresFormas(f * f, n * n) : "0") + T("; without replacement ", "; sin reemplazo ") + (f >= 2 ? tresFormas(f * (f - 1), n * (n - 1)) : "0") + ".</div>";
  $("pr-res").innerHTML = h;
}
/* (F) Saving */
var CAMPOS = ["p-nombre", "p-fecha", "p-titulo", "p-unidad", "p-fuente", "est-trabajo", "gr-tipo", "gr-inicio", "gr-ancho", "gr-texto", "in-texto", "pr-pregunta", "pr-cond", "pr-v1", "pr-v2", "pr-trabajo"];
function guarda(){
  var e = {datos: valoresCrudos(), cierre: [].map.call(document.querySelectorAll(".lista-cierre input"), function(c){ return c.checked; })};
  CAMPOS.forEach(function(id){ e[id] = $(id).value; });
  try { localStorage.setItem(CLAVE, JSON.stringify(e)); $("guardado").textContent = T("Saved in this browser at ", "Guardado en este navegador a las ") + new Date().toLocaleTimeString(ES ? "es" : "en-US", {hour: "2-digit", minute: "2-digit"}) + "."; }
  catch (err){ $("guardado").textContent = T("This browser cannot save. Export to PDF to keep your work.", "Este navegador no puede guardar. Exporte a PDF para conservar su trabajo."); }
}
function restaura(){
  var e = null; try { e = JSON.parse(localStorage.getItem(CLAVE) || "null"); } catch (err){}
  if (!e){ pintaRejilla(new Array(12).fill("")); return; }
  CAMPOS.forEach(function(id){ if (e[id] !== undefined) $(id).value = e[id]; });
  pintaRejilla(e.datos && e.datos.length ? e.datos : new Array(12).fill(""));
  [].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c, i){ c.checked = !!(e.cierre && e.cierre[i]); });
}
var temporizador = null;
function todo(){
  var d = valores(), E = estadisticos(d);
  pintaEst(E, d); pintaGraf(E, d); pintaProb(d);
  var k = oraciones($("in-texto").value); $("in-cuenta").textContent = T("Sentences found: ", "Oraciones detectadas: ") + k + (k < 5 ? T(" (write at least 5)", " (escriba al menos 5)") : " ✓");
  clearTimeout(temporizador); temporizador = setTimeout(guarda, 500);
}
CAMPOS.forEach(function(id){ $(id).addEventListener("input", todo); $(id).addEventListener("change", todo); });
[].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c){ c.addEventListener("change", guarda); });
$("gr-sugerir").addEventListener("click", function(){ sugerir(valores()); todo(); });
$("b-pdf").addEventListener("click", function(){ document.querySelectorAll("details.modulo").forEach(function(x){ x.open = true; }); window.print(); });
window.addEventListener("beforeprint", function(){ document.querySelectorAll("details.modulo").forEach(function(x){ x.open = true; }); });
$("b-borrar").addEventListener("click", function(){ $("b-borrar").hidden = true; $("b-borrar-si").hidden = false; $("b-borrar-no").hidden = false; $("borrar-msg").textContent = T("Erase all your work? This cannot be undone.", "¿Borrar todo su trabajo? No se puede deshacer."); });
$("b-borrar-no").addEventListener("click", function(){ $("b-borrar").hidden = false; $("b-borrar-si").hidden = true; $("b-borrar-no").hidden = true; $("borrar-msg").textContent = ""; });
$("b-borrar-si").addEventListener("click", function(){ try { localStorage.removeItem(CLAVE); } catch (err){} CAMPOS.forEach(function(id){ var x = $(id); if (x.tagName === "SELECT") x.selectedIndex = 0; else x.value = ""; }); [].forEach.call(document.querySelectorAll(".lista-cierre input"), function(c){ c.checked = false; }); pintaRejilla(new Array(12).fill("")); $("b-borrar-no").click(); todo(); });
restaura(); todo();
'''

def pagina():
    def campo(i, et, tipo="text", extra=""):
        return f'<div class="campo" style="flex:1;min-width:220px;"><label for="{i}">{et}</label><input type="{tipo}" id="{i}" autocomplete="off" {extra}></div>'
    rub = [(t("1. Data set", "1. Conjunto de datos"), t("Made-up data, or data with no description.", "Datos inventados o sin describir."), t("Real data, but with no clear source.", "Datos reales, pero sin fuente clara."), t("A real data set, well described.", "Conjunto de datos real y bien descrito."), t("Real, relevant data, with the source and context explained.", "Datos reales, relevantes y con su fuente y contexto explicados.")),
           (t("2. Graph", "2. Representación gráfica"), t("No valid graph.", "No incluye una gráfica válida."), t("A graph with mistakes or no labels.", "Gráfica con errores o sin etiquetas."), t("A correct box plot or histogram with all its labels.", "Caja o histograma correcto con todas las etiquetas."), t("A clear, correct, well-labeled graph that fits the data.", "Gráfica clara, correcta y bien rotulada, adecuada a los datos.")),
           (t("3. Statistics", "3. Cálculo de estadísticos"), t("No statistics.", "No calcula estadísticos."), t("Fewer than three, or with mistakes.", "Calcula menos de tres o con errores."), t("At least three correct statistics.", "Calcula correctamente al menos tres estadísticos."), t("Several statistics with no mistakes, connected to each other.", "Calcula varios estadísticos sin errores y los relaciona entre sí.")),
           (t("4. Written interpretation", "4. Interpretación escrita"), t("No interpretation.", "No interpreta los datos."), t("A vague interpretation, or one that does not match the data.", "Interpretación vaga o incoherente con los datos."), t("A written interpretation that matches the data.", "Interpretación escrita coherente con los datos."), t("A clear, deep interpretation (center, spread, and shape).", "Interpretación clara y profunda (centro, dispersión y forma).")),
           (t("5. Probability", "5. Cálculo de probabilidad"), t("No probability.", "No incluye probabilidad."), t("A probability with mistakes.", "Cálculo de probabilidad con errores."), t("A correct probability connected to the context.", "Cálculo de probabilidad correcto vinculado al contexto."), t("A correct probability, well explained and connected to the analysis.", "Probabilidad correcta, bien explicada y ligada al análisis."))]
    filas_rub = "".join("<tr><th scope=\"row\">" + r[0] + "</th>" + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in rub)
    cierre = [t("<strong>Complete and saved as a PDF</strong>, with the five parts: data, graph, statistics, interpretation, and probability. It is your proof that you finished Level 3.", "<strong>Proyecto completo y guardado en PDF</strong>, con los cinco componentes: datos, gráfica, estadísticos, interpretación y probabilidad. Es su constancia de haber terminado el Nivel 3."),
              t("<strong>Explained out loud</strong> for three or four minutes, to someone in your family or recording yourself on your phone. Say where the data came from, what the graph shows, and what you conclude. What you cannot explain out loud, you do not fully understand yet.", "<strong>Explicado en voz alta</strong>, de tres a cuatro minutos, a un familiar o grabándose con el teléfono. Diga de dónde salieron los datos, qué muestra la gráfica y qué concluye. Lo que no logre explicar en voz alta todavía no lo entendió del todo."),
              t("<strong>Reviewed the next day</strong> with the rubric below in hand, criterion by criterion, as if the work were someone else's.", "<strong>Revisado al día siguiente</strong> con la rúbrica de abajo en la mano, criterio por criterio, como si el trabajo fuera de otra persona."),
              t("<strong>GED formula sheet reviewed</strong> before the final check of the level. You will have it on the test, but looking for a formula takes time: it pays to know where each one is.", "<strong>Hoja de fórmulas del GED repasada</strong> antes de la evaluación final del nivel. En el examen la tendrá disponible, pero buscar una fórmula cuesta tiempo: conviene saber dónde está cada una.")]
    conds = "".join(f'<option value="{k}">{v}</option>' for k, v in (("mayor", t("Greater than (>)", "Mayor que (>)")), ("mayorIg", t("Greater than or equal to (≥)", "Mayor o igual que (≥)")), ("menor", t("Less than (<)", "Menor que (<)")), ("menorIg", t("Less than or equal to (≤)", "Menor o igual que (≤)")), ("igual", t("Equal to (=)", "Igual a (=)")), ("entre", t("Between two values (inclusive)", "Entre dos valores (inclusive)"))))
    mods = [
     (t("instructions", "instrucciones"), t("Project instructions", "Instrucciones del proyecto"),
      f'''      <p>{t("This project brings together what you learned in the eight topics of Level 3, and it is the last piece of the level. Here the separate skills are all used on the same data: yours. Take your time; it is not one more exercise, it is the proof that you learned the level.", "Este proyecto reúne lo aprendido en los ocho temas del Nivel 3 y es la última pieza del nivel. Aquí las destrezas sueltas se usan todas sobre unos mismos datos: los suyos. Tómeselo con calma; no es un ejercicio más, es la prueba de que el nivel quedó aprendido.")}</p>
      <p>{t("Choose a real data set from your own life (your expenses for a month, the ages in your family, the temperatures of the week, your grades for the semester) and analyze it completely. The project must include five parts:", "Elija un conjunto de datos real de su propio entorno (los gastos de un mes, las edades de su familia, las temperaturas de la semana, las calificaciones del semestre) y analícelo por completo. El proyecto debe incluir cinco componentes:")}</p>
      <ol><li>{t("<strong>Data set:</strong> 10 to 20 real values, with their source and context described.", "<strong>Conjunto de datos:</strong> entre 10 y 20 valores reales, con su fuente y su contexto descritos.")}</li>
      <li>{t("<strong>Graph:</strong> a box plot or a histogram, with all its labels.", "<strong>Gráfica:</strong> un diagrama de caja y bigotes o un histograma, con todas sus etiquetas.")}</li>
      <li>{t("<strong>Statistics:</strong> at least three calculations (mean, median, IQR, or another).", "<strong>Estadísticos:</strong> al menos tres cálculos (media, mediana, IQR u otro).")}</li>
      <li>{t("<strong>Written interpretation:</strong> what the data say about their center, spread, and shape.", "<strong>Interpretación escrita:</strong> qué dicen los datos sobre su centro, su dispersión y su forma.")}</li>
      <li>{t("<strong>Probability:</strong> at least one probability calculation connected to the context of the data.", "<strong>Probabilidad:</strong> al menos un cálculo de probabilidad vinculado al contexto de los datos.")}</li></ol>
      <div class="caja-tip">{t("The template calculates the statistics, draws the graph, and offers checks, but <strong>you must show your work in writing</strong>: the automatic calculation is only there to check yours.", "La plantilla calcula los estadísticos, construye la gráfica y ofrece comprobaciones, pero <strong>usted debe mostrar su procedimiento por escrito</strong>: el cálculo automático solo sirve para verificar el suyo.")}</div>
      <div class="fila-btn no-imp"><button type="button" class="btn" id="b-pdf">{t("Export as PDF", "Exportar como PDF")}</button><button type="button" class="btn-sec" id="b-borrar">{t("Erase everything", "Borrar todo")}</button><button type="button" class="btn" id="b-borrar-si" hidden>{t("Yes, erase", "Sí, borrar")}</button><button type="button" class="btn-sec" id="b-borrar-no" hidden>{t("No, keep it", "No, conservar")}</button></div>
      <p class="nota" id="borrar-msg" role="status"></p>
      <p class="guardado" id="guardado" aria-live="polite">{t("Your work is saved only in this browser. To keep it, press “Export as PDF” and choose “Save as PDF” as the destination.", "Su trabajo se guarda solo en este navegador. Para conservarlo, pulse «Exportar como PDF» y elija «Guardar como PDF» como destino.")}</p>'''),
     (t("student", "estudiante"), t("0 · About you and the data set", "0 · Datos del estudiante y del conjunto"),
      f'''      <div class="campos">{campo("p-nombre", t("Student's name", "Nombre del estudiante"))}{campo("p-fecha", t("Due date", "Fecha de entrega"), "date")}</div>
      <div class="campos">{campo("p-titulo", t("Title of the data set", "Título del conjunto de datos"))}{campo("p-unidad", t("Unit of measure (for example, dollars, °F, minutes)", "Unidad de medida (por ejemplo, dólares, °F, minutos)"))}</div>
      <div class="campo"><label for="p-fuente">{t("Source and context of the data", "Fuente y contexto de los datos")}</label><textarea class="trabajo" id="p-fuente" style="min-height:90px"></textarea></div>'''),
     (t("data", "datos"), t("1 · Data set", "1 · Conjunto de datos"),
      f'''      <p>{t("Type 10 to 20 real numerical values. The template puts them in order and calculates everything else from them.", "Escriba entre 10 y 20 valores numéricos reales. La plantilla los ordena de menor a mayor y calcula todo lo demás a partir de ellos.")}</p>
      <div class="rejilla" id="rejilla"></div>
      <div class="fila-btn no-imp"><button type="button" class="btn-sec" id="dt-mas">{t("＋ Add a value", "＋ Agregar dato")}</button><button type="button" class="btn-sec" id="dt-menos">{t("− Remove the last one", "− Quitar el último")}</button></div>
      <div class="no-imp"><div class="campo"><label for="dt-pegar">{t("Optional shortcut: paste your data here, separated by commas or spaces", "Atajo opcional: pegue aquí sus datos separados por comas o espacios")}</label><textarea class="trabajo" id="dt-pegar" style="min-height:60px"></textarea></div>
      <div class="fila-btn"><button type="button" class="btn-sec" id="dt-cargar">{t("Load the pasted data", "Cargar los datos pegados")}</button></div></div>
      <p class="caja-aviso" id="dt-aviso" role="alert"></p>
      <p><strong id="dt-cuenta"></strong></p>
      <p>{t("Data in order from least to greatest:", "Datos ordenados de menor a mayor:")}</p><div id="dt-orden">—</div>'''),
     (t("statistics", "estadisticos"), t("2 · Statistics", "2 · Cálculo de estadísticos"),
      f'''      <p>{t("Find at least three statistics by hand and show the whole process, not only the answer. The check panel is only for checking your work.", "Calcule al menos tres estadísticos a mano y muestre el procedimiento completo, no solo el resultado. El panel de comprobación sirve únicamente para verificar su trabajo.")}</p>
      <div class="campo"><label for="est-trabajo">{t("Your process and results (write here)", "Procedimiento y resultados (escriba aquí)")}</label><textarea class="trabajo" id="est-trabajo"></textarea></div>
      <h3>{t("Automatic check (from the data in section 1)", "Comprobación automática (a partir de los datos de la sección 1)")}</h3>
      <div class="tabla-scroll"><table class="tabla-est" id="est-tabla"></table></div>
      <p class="nota">{t("The quartiles use the method of the course: put the data in order, the median splits them into two halves, and Q1 and Q3 are the medians of the lower and upper halves (if n is odd, the median goes into neither half).", "Los cuartiles se calculan con el método del curso: se ordena el conjunto, la mediana lo divide en dos mitades y Q1 y Q3 son las medianas de la mitad inferior y de la superior (si n es impar, la mediana no se incluye en ninguna mitad).")}</p>
      <p id="est-lim"></p>'''),
     (t("graph", "grafica"), t("3 · Graph", "3 · Representación gráfica"),
      f'''      <p>{t("Choose a box plot or a histogram. The graph is built from the data in section 1 and includes all its labels.", "Elija un diagrama de caja y bigotes o un histograma. La gráfica se construye con los datos de la sección 1 e incluye todas sus etiquetas.")}</p>
      <div class="campos"><div class="campo"><label for="gr-tipo">{t("Kind of graph", "Tipo de gráfica")}</label><select id="gr-tipo"><option value="caja">{t("Box plot", "Diagrama de caja y bigotes")}</option><option value="hist">{t("Histogram", "Histograma")}</option></select></div></div>
      <div id="gr-hist" hidden><div class="campos"><div class="campo"><label for="gr-inicio">{t("Start of the first interval", "Inicio del primer intervalo")}</label><input type="text" inputmode="decimal" class="corto" id="gr-inicio" value="0"></div>
        <div class="campo"><label for="gr-ancho">{t("Width of the intervals", "Ancho del intervalo")}</label><input type="text" inputmode="decimal" class="corto" id="gr-ancho" value="10"></div>
        <div class="fila-btn no-imp" style="align-self:flex-end;"><button type="button" class="btn-sec" id="gr-sugerir">{t("Suggest intervals", "Sugerir intervalos")}</button></div></div></div>
      <div id="gr-svg"></div>
      <div class="campo"><label for="gr-texto">{t("Title of the graph and why you chose it", "Título de la gráfica y explicación de su elección")}</label><textarea class="trabajo" id="gr-texto" style="min-height:90px"></textarea></div>'''),
     (t("interpretation", "interpretacion"), t("4 · Written interpretation", "4 · Interpretación escrita"),
      f'''      <p>{t("Write at least five complete sentences. A graph with no interpretation is incomplete: explain what your data say.", "Redacte al menos cinco oraciones completas. Una gráfica sin interpretación queda incompleta: explique qué dicen sus datos.")}</p>
      <div class="caja-tip"><strong>{t("Writing guide: the three things to cover", "Guía de redacción: los tres aspectos que debe cubrir")}</strong><ul>
        <li>{t("<strong>Center:</strong> around what value are the data grouped? (mean, median)", "<strong>Centro:</strong> ¿alrededor de qué valor se agrupan los datos? (media, mediana)")}</li>
        <li>{t("<strong>Spread:</strong> how far apart are they? (range, IQR, length of the whiskers)", "<strong>Dispersión:</strong> ¿qué tan separados están? (rango, IQR, longitud de los bigotes)")}</li>
        <li>{t("<strong>Shape:</strong> are they spread evenly, are they pulled to one side, are there unusually high or low values?", "<strong>Forma:</strong> ¿se reparten de manera simétrica, se cargan hacia un lado, hay valores llamativamente altos o bajos?")}</li>
        <li>{t("End with a conclusion of your own: what did you learn about the situation you measured?", "Cierre con una conclusión propia: ¿qué aprendió sobre la situación que midió?")}</li></ul></div>
      <div class="campo"><label for="in-texto">{t("Your interpretation", "Su interpretación")}</label><textarea class="trabajo" id="in-texto" style="min-height:200px"></textarea></div>
      <p class="nota" id="in-cuenta" aria-live="polite"></p>'''),
     (t("probability", "probabilidad"), t("5 · Probability", "5 · Cálculo de probabilidad"),
      f'''      <p>{t("Ask at least one probability question about your own data set and answer it. Write the answer as a fraction, a decimal, and a percent.", "Plantee al menos una pregunta de probabilidad sobre su propio conjunto de datos y resuélvala. Exprese el resultado en fracción, decimal y porcentaje.")}</p>
      <div class="campo"><label for="pr-pregunta">{t("The probability question you will answer", "Pregunta de probabilidad que va a resolver")}</label><textarea class="trabajo" id="pr-pregunta" style="min-height:70px"></textarea></div>
      <h3>{t("Automatic check of the probability", "Comprobación automática de la probabilidad")}</h3>
      <div class="campos"><div class="campo"><label for="pr-cond">{t("Condition for a favorable value", "Condición del evento favorable")}</label><select id="pr-cond">{conds}</select></div>
        <div class="campo"><label for="pr-v1">{t("Reference value", "Valor de referencia")}</label><input type="text" inputmode="decimal" class="corto" id="pr-v1"></div>
        <div class="campo" id="pr-v2c" hidden><label for="pr-v2">{t("Second value", "Segundo valor")}</label><input type="text" inputmode="decimal" class="corto" id="pr-v2"></div></div>
      <div class="salida" id="pr-res" aria-live="polite"></div>
      <div class="campo"><label for="pr-trabajo">{t("Setup and solution (write here)", "Planteamiento y resolución (escriba aquí)")}</label><textarea class="trabajo" id="pr-trabajo"></textarea></div>'''),
     (t("finish", "cierre"), t("✓ How to finish the project", "✓ Cómo cerrar el proyecto"),
      f'''      <p>{t("Check each step as you finish it. All four matter; the second one is what really shows whether you understood.", "Marque lo que vaya completando. Los cuatro pasos importan; el segundo es el que de verdad revela si entendió.")}</p>
      <div class="lista-cierre">{"".join(f'<label><input type="checkbox"><span>{c}</span></label>' for c in cierre)}</div>'''),
     (t("rubric", "rubrica"), t("Project rubric", "Rúbrica del proyecto"),
      f'''      <p>{t("Five criteria at four levels (20 points in all). Read them before you start, and come back to them when you finish to grade your own work honestly.", "Cinco criterios en cuatro niveles de desempeño (20 puntos en total). Léalos antes de empezar y vuelva a ellos al terminar, para evaluar su propio trabajo con honestidad.")}</p>
      <div class="tabla-scroll"><table class="tabla-est"><caption class="sr-only">{t("Rubric for the final project, with five criteria and four levels", "Rúbrica del proyecto final, con cinco criterios y cuatro niveles")}</caption>
        <thead><tr><th scope="col">{t("Criterion", "Criterio")}</th><th scope="col">{t("Beginning (1)", "Inicial (1)")}</th><th scope="col">{t("Developing (2)", "En desarrollo (2)")}</th><th scope="col">{t("Proficient (3)", "Competente (3)")}</th><th scope="col">{t("Outstanding (4)", "Destacado (4)")}</th></tr></thead>
        <tbody>{filas_rub}</tbody></table></div>
      <p class="nota">{t("The project grade is combined with the grade on the Level 3 final check (25 questions).", "La nota del proyecto se combina con la de la evaluación final del Nivel 3 (25 preguntas).")}</p>''')]
    meta = t("Your work template for the Level 3 final project. Fill it in, check your work, and save it as a PDF.", "Su plantilla de trabajo para el proyecto final del Nivel 3. Complétela, compruebe su trabajo y guárdela en PDF.")
    return B.pagina_practica("8-3", 8, t(*TEMA), t("Final project: My data analysis", "Proyecto final: Mi análisis de datos"), meta, mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

def construye():
    html = {}
    for lang in ("en", "es"):
        B.L = lang
        s = pagina()
        s = s.replace(f'<h1>{t("Lesson", "Lección")} 8.3 · {t("Final project: My data analysis", "Proyecto final: Mi análisis de datos")}</h1>', f'<h1>{t("Final project · My data analysis", "Proyecto final · Mi análisis de datos")}</h1>')
        s = s.replace(f'<title>{t("Practice · Lesson", "Práctica · Lección")} 8.3 · ', f'<title>{t("Final project", "Proyecto final")} · {t("Lesson", "Lección")} 8.3 · ')
        s = s.replace('<a class="lg-link" href="./">Math · Level 3 lessons</a>', f'<a class="lg-link" href="{t("lesson-8-3", "leccion-8-3")}.html">{t("← Back to Lesson 8.3", "← Volver a la Lección 8.3")}</a>')
        s = s.replace("practice (English) — built by", "final project template (English) — built by")
        html[lang] = s
    B.L = "en"
    ruta_en = "math/level-3/project-level-3.html"
    open(os.path.join(ROOT, ruta_en), "w", encoding="utf-8").write(html["en"]); print("ok", ruta_en)
    tr = Traductor(ruta_en, texto=html["es"], nivel=3); tr.frecuentes()
    tr.cabecera("<!-- LearnGED · Nivel 3 · Lección 8.3 · Proyecto final «Mi análisis de datos» — plantilla (español) — construida con tools/build_n3_proyecto.py\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
    ruta_es = "es/matematicas/nivel-3/proyecto-nivel-3.html"
    tr.guarda(ruta_es)
    s = open(os.path.join(ROOT, ruta_es), encoding="utf-8").read()
    for frase in ["Back to contents", "On this page", "Open all"]:
        if frase in s: print("  ¡OJO! queda en inglés en", ruta_es, ":", frase)

if __name__ == "__main__":
    construye()
