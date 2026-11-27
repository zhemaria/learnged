"""LearnGED · Estudios sociales · Simulacro cronometrado (Lección 8.3) — página en inglés y en español.
  social-studies/practice-test.html · es/estudios-sociales/simulacro.html
Reúne las preguntas tipo GED de las lecciones de contenido (Temas 3 a 7, más las de la 8.1 y la 8.3 que no dependen de la lección):
se ejecuta cada builder, se capturan sus llamadas a ciencia.ged_item y se descartan las que remiten a una sección, a un documento
o a una gráfica de su lección. Cada intento elige 35 preguntas con la distribución del examen (18 de cívica y gobierno, 7 de historia
de los EE. UU., 5 de economía y 5 de geografía), 70 minutos con reloj, control de ritmo en el minuto 35, preguntas marcadas para
revisar, envío automático al acabar el tiempo e informe por dominio y por práctica de estudios sociales.
Uso: python3 tools/build_soc_simulacro.py  (después de construir las lecciones)
"""
import os, sys, re, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, NOMBRE_SSP

EXCLUYE = re.compile(r"section \d|Document|in this lesson|Look at|Read Ad|On the GED", re.I)
LECCIONES = [f"{a}-{b}" for a in range(3, 8) for b in (1, 2, 3)] + ["8-1", "8-3"]
DOM_LEC = {"3": "civics", "4": "civics", "5-1": "civics", "5-2": "civics", "5-3": "economics", "6": "history", "7-1": "economics", "7-2": "geography", "7-3": "geography", "8-1": "history", "8-3": "civics"}
DOM_ITEM = {("8-1", 5): "geography", ("8-3", 2): "economics", ("8-3", 3): "economics"}
CUOTA = {"civics": 18, "history": 7, "economics": 5, "geography": 5}


def dominio(n, num):
    return DOM_ITEM.get((n, num)) or DOM_LEC.get(n) or DOM_LEC[n[0]]


def recoge():
    orig = C.ged_item
    cap = []
    C.ged_item = lambda P, num, sp, dok, preg, ops, ok, pistas, sol: (cap.append((num, sp, dok, preg, ops, ok, pistas, sol)), orig(P, num, sp, dok, preg, ops, ok, pistas, sol))[1]
    items = []
    for n in LECCIONES:
        m = importlib.import_module("build_soc_" + n.replace("-", "_"))
        por = {}
        for lang in ("en", "es"):
            C.L = lang
            cap.clear()
            m.leccion()
            por[lang] = list(cap)
        for k, (en, es) in enumerate(zip(por["en"], por["es"])):
            if EXCLUYE.search(re.sub("<[^>]+>", " ", en[3])):
                continue
            items.append({"lec": n, "dom": dominio(n, en[0]), "sp": en[1], "dok": en[2],
                          "q": {"en": en[3], "es": es[3]}, "ops": {"en": en[4], "es": es[4]}, "ok": en[5],
                          "pistas": {"en": {str(i): h for i, h in en[6].items()}, "es": {str(i): h for i, h in es[6].items()}},
                          "sol": {"en": en[7], "es": es[7]}})
    C.ged_item = orig
    C.L = "en"
    return items


SP = [(k, v[0], v[1]) for k, v in NOMBRE_SSP.items()]
_LEER = ("Reading the source is the problem, not the content: go back to Topic 1 (sources, point of view) and Lesson 8.1.", "La dificultad está en leer la fuente, no en el contenido: repase el Tema 1 (fuentes, punto de vista) y la Lección 8.1.")
_DATOS = ("The obstacle is working with numbers and graphs: review Topic 2 (graphs, percents, rates, center).", "El obstáculo son los números y las gráficas: repase el Tema 2 (gráficas, porcentajes, tasas, medidas de centro).")
_RAZ = ("You know the content but deciding what the evidence supports is harder: review Lessons 1.3 and 8.1 (absolutes, period, population, and unit).", "El contenido se domina, pero cuesta decidir qué sostiene la evidencia: repase las lecciones 1.3 y 8.1 (absolutos, periodo, población y unidad).")
_CAUSA = ("Cause and effect is the weak spot: review Lessons 6.1 to 6.3 (immediate and structural causes) and 7.1 (markets).", "El punto débil es la causa y el efecto: repase las lecciones 6.1 a 6.3 (causas inmediatas y estructurales) y la 7.1 (mercados).")
GUIA = {"SSP.1": _LEER, "SSP.2": _LEER, "SSP.4": ("Words in context: reread the document excerpts of Topics 3 and 4 and look up the terms in each glossary.", "Palabras en contexto: relea los fragmentos de documentos de los Temas 3 y 4 y repase los términos de cada glosario."),
        "SSP.5": ("Point of view and purpose: review Lessons 1.2 and 1.3.", "Punto de vista y propósito: repase las lecciones 1.2 y 1.3."), "SSP.3": _CAUSA, "SSP.6": _DATOS, "SSP.10": _DATOS, "SSP.11": _DATOS, "SSP.7": _RAZ, "SSP.8": _RAZ}
DOMS = [("civics", "Civics and government", "Educación cívica y gobierno"), ("history", "U.S. history", "Historia de los EE. UU."), ("economics", "Economics", "Economía"), ("geography", "Geography and the world", "Geografía y el mundo")]

LOGICA = r'''
var D = window.SIM, ES = D.es, X = D.txt, TOTAL = 35, SEG = 70 * 60;
function $(id){ return document.getElementById(id); }
function baraja(a){ a = a.slice(); for (var i = a.length - 1; i > 0; i--){ var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
var PREG = [], fin = 0, reloj = null, enviado = false, avisos = {};
function lec(l){ return (ES ? "leccion-" : "lesson-") + l + ".html"; }
function elige(){
  var sel = [];
  Object.keys(D.cuota).forEach(function(d){ sel = sel.concat(baraja(D.items.filter(function(q){ return q.dom === d; })).slice(0, D.cuota[d])); });
  return baraja(sel).map(function(q){ return {q: q, orden: baraja(q.ops.map(function(_, j){ return j; })), elegida: null, marca: false}; });
}
function pinta(){
  var c = $("preguntas"); c.innerHTML = "";
  PREG.forEach(function(p, i){
    var f = document.createElement("fieldset"); f.className = "pregunta-c"; f.id = "q-" + (i + 1);
    f.innerHTML = "<legend><span class=\"num\">" + (i + 1) + "</span> <span class=\"sr-only\">" + X.preg + " " + (i + 1) + X.de + TOTAL + ". </span></legend><div class=\"enun\">" + p.q.q + "</div>";
    var o = document.createElement("div"); o.className = "opciones"; o.setAttribute("role", "group"); o.setAttribute("aria-label", X.opciones + " " + (i + 1));
    p.orden.forEach(function(j){
      var b = document.createElement("button"); b.type = "button"; b.className = "opcion"; b.setAttribute("aria-pressed", "false"); b.innerHTML = p.q.ops[j];
      b.addEventListener("click", function(){ if (enviado) return; p.elegida = j; [].forEach.call(o.children, function(x){ x.setAttribute("aria-pressed", "false"); x.classList.remove("elegida"); }); b.setAttribute("aria-pressed", "true"); b.classList.add("elegida"); estado(); });
      o.appendChild(b);
    });
    f.appendChild(o);
    var m = document.createElement("label"); m.className = "marca"; m.innerHTML = "<input type=\"checkbox\"> " + X.marcar;
    m.querySelector("input").addEventListener("change", function(e){ p.marca = e.target.checked; estado(); });
    f.appendChild(m);
    var fb = document.createElement("div"); fb.className = "fb"; fb.setAttribute("role", "status"); f.appendChild(fb);
    c.appendChild(f);
  });
  var nav = $("mapa"); nav.innerHTML = "";
  PREG.forEach(function(p, i){ var a = document.createElement("a"); a.href = "#q-" + (i + 1); a.textContent = i + 1; a.id = "m-" + (i + 1); nav.appendChild(a); });
  estado();
}
function estado(){
  var r = PREG.filter(function(p){ return p.elegida !== null; }).length, m = PREG.filter(function(p){ return p.marca; }).length;
  $("contador").textContent = X.resp + r + X.de + TOTAL + (m ? " · " + X.marcadas + m : "");
  PREG.forEach(function(p, i){ var a = $("m-" + (i + 1)); if (!a) return; a.className = (p.elegida !== null ? "hecha" : "") + (p.marca ? " marcada" : ""); a.setAttribute("aria-label", X.preg + " " + (i + 1) + ": " + (p.elegida !== null ? X.respondida : X.sinresp) + (p.marca ? ", " + X.marcada : "")); });
}
function mmss(s){ s = Math.max(0, Math.round(s)); var m = Math.floor(s / 60), x = s % 60; return m + ":" + (x < 10 ? "0" : "") + x; }
function tic(){
  var q = (fin - Date.now()) / 1000; $("reloj").textContent = mmss(q);
  var usado = SEG - q, r = PREG.filter(function(p){ return p.elegida !== null; }).length;
  [[35, 17], [55, 27]].forEach(function(h){ if (usado >= h[0] * 60 && !avisos[h[0]]){ avisos[h[0]] = 1; if (r < h[1]) anuncia(X.ritmo1 + h[0] + X.ritmo2 + h[1] + X.ritmo3); } });
  [[10, X.quedan10], [5, X.quedan5], [1, X.quedan1]].forEach(function(h){ if (q <= h[0] * 60 && !avisos["q" + h[0]]){ avisos["q" + h[0]] = 1; anuncia(h[1]); } });
  if (q <= 0){ clearInterval(reloj); anuncia(X.tiempo); envia(true); }
}
function anuncia(m){ var a = $("aviso-reloj"); a.textContent = m; a.className = "aviso-reloj visible"; }
function empieza(){
  PREG = elige(); pinta(); enviado = false; avisos = {};
  $("antes").hidden = true; $("examen").hidden = false; $("informe").hidden = true; $("resultado").textContent = ""; $("aviso-reloj").className = "aviso-reloj"; $("aviso-reloj").textContent = "";
  fin = Date.now() + SEG * 1000; clearInterval(reloj); reloj = setInterval(tic, 1000); tic();
  $("q-1").scrollIntoView(); $("reloj-caja").focus();
}
function envia(auto){
  if (enviado) return;
  var sin = PREG.filter(function(p){ return p.elegida === null; }).length;
  if (!auto && sin && !$("b-enviar").dataset.aviso){ $("b-enviar").dataset.aviso = "1"; anuncia(X.sin1 + sin + X.sin2); return; }
  enviado = true; clearInterval(reloj); delete $("b-enviar").dataset.aviso;
  var usado = Math.min(SEG, SEG - (fin - Date.now()) / 1000), ok = 0, pd = {}, ps = {}, mal = {};
  var fs = $("preguntas").querySelectorAll("fieldset");
  PREG.forEach(function(p, i){
    var q = p.q, bien = p.elegida === q.ok, sp = q.sp.split(".").slice(0, 2).join(".");
    pd[q.dom] = pd[q.dom] || {c: 0, t: 0}; pd[q.dom].t++; ps[sp] = ps[sp] || {c: 0, t: 0, l: []}; ps[sp].t++;
    if (bien){ ok++; pd[q.dom].c++; ps[sp].c++; } else { if (ps[sp].l.indexOf(q.lec) < 0) ps[sp].l.push(q.lec); mal[q.lec] = 1; }
    var bs = fs[i].querySelectorAll(".opcion");
    p.orden.forEach(function(j, k){ bs[k].disabled = true; if (j === q.ok) bs[k].classList.add("correcta"); if (j === p.elegida && !bien) bs[k].classList.add("incorrecta"); });
    fs[i].querySelector(".marca").hidden = true;
    var pista = (!bien && p.elegida !== null && q.pistas[p.elegida]) ? " " + q.pistas[p.elegida] : "";
    var fb = fs[i].querySelector(".fb"); fb.className = "fb " + (bien ? "bien" : "mal");
    fb.innerHTML = "<strong>" + (bien ? X.correcto : (p.elegida === null ? X.sinresp2 : X.incorrecto)) + "</strong>" + pista + " " + q.sol + " <span class=\"meta-q\">" + q.sp + " · DOK " + q.dok + " · <a href=\"" + lec(q.lec) + "\">" + X.leccion + " " + q.lec.replace("-", ".") + "</a></span>";
  });
  var pct = Math.round(ok / TOTAL * 100);
  $("resultado").innerHTML = X.puntaje + "<strong>" + ok + X.de + TOTAL + "</strong> (" + pct + " %) · " + X.tiempoUsado + mmss(usado) + ". " + (pct > 75 ? X.rmas : (pct >= 65 ? X.r75 : (pct >= 50 ? X.r65 : X.r50)));
  $("t-dom").innerHTML = D.doms.map(function(d){ var x = pd[d[0]] || {c: 0, t: 0}; var p = x.t ? Math.round(x.c / x.t * 100) : 0; return "<tr><th scope=\"row\">" + d[1] + "</th><td>" + x.c + X.de + x.t + "</td><td>" + p + " %</td></tr>"; }).join("");
  $("t-sp").innerHTML = D.sps.filter(function(s){ return ps[s[0]]; }).map(function(s){ var x = ps[s[0]], p = Math.round(x.c / x.t * 100), j = p === 100 ? X.dominado : (p >= 60 ? X.desarrollo : X.repaso);
    return "<tr><th scope=\"row\">" + s[0] + " · " + s[1] + "</th><td>" + x.c + X.de + x.t + "</td><td>" + p + " %</td><td>" + j + (p < 100 ? ". " + D.guia[s[0]] + (x.l.length ? " " + X.repase + x.l.map(function(l){ return "<a href=\"" + lec(l) + "\">" + X.leccion + " " + l.replace("-", ".") + "</a>"; }).join(", ") + "." : "") : "") + "</td></tr>"; }).join("");
  $("informe").hidden = false; $("b-enviar").hidden = true; $("acciones-fin").hidden = false;
  $("nombre-imp").textContent = ($("nombre").value.trim() ? $("nombre").value.trim() + " · " : "") + new Date().toLocaleDateString(ES ? "es" : "en-US", {year: "numeric", month: "long", day: "numeric"});
  $("resultado").focus();
}
$("b-empezar").addEventListener("click", empieza);
$("b-enviar").addEventListener("click", function(){ envia(false); });
$("b-otra").addEventListener("click", function(){ $("acciones-fin").hidden = true; $("b-enviar").hidden = false; empieza(); });
$("b-imprimir").addEventListener("click", function(){ window.print(); });
window.addEventListener("beforeunload", function(e){ if (reloj && !enviado){ e.preventDefault(); e.returnValue = ""; } });
'''

ESTILO = """
  [hidden]{display:none !important;}
  .lg-bar{position:static !important;}
  .barra-reloj{position:sticky;top:0;z-index:20;background:#26324a;color:#fff;display:flex;flex-wrap:wrap;gap:10px 20px;align-items:center;justify-content:space-between;padding:10px 16px;border-radius:0 0 10px 10px;margin:0 0 12px;}
  .barra-reloj .reloj{font-size:24px;font-weight:700;font-variant-numeric:tabular-nums;}
  .barra-reloj .btn-env{background:#fff;color:#26324a;border:0;border-radius:8px;padding:8px 16px;font-weight:700;font-size:16px;cursor:pointer;}
  .aviso-reloj{display:none;margin:0 0 12px;padding:10px 14px;background:#fff8e1;border-left:6px solid #f9a825;border-radius:8px;font-weight:600;}
  .aviso-reloj.visible{display:block;}
  nav.mapa{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 16px;}
  nav.mapa a{display:inline-flex;width:34px;height:34px;align-items:center;justify-content:center;border:2px solid #b0bec5;border-radius:6px;text-decoration:none;color:#26324a;font-weight:700;background:#fff;}
  nav.mapa a.hecha{background:#d9e6ff;border-color:#1e3a8a;}
  nav.mapa a.marcada{box-shadow:inset 0 -5px 0 #f9a825;}
  fieldset.pregunta-c{border:2px solid #dfe3ee;border-radius:12px;padding:14px 18px;margin:16px 0;background:#fff;scroll-margin-top:70px;}
  fieldset.pregunta-c legend .num{display:inline-flex;width:32px;height:32px;align-items:center;justify-content:center;border-radius:50%;background:#26324a;color:#fff;font-weight:700;}
  .opciones{display:flex;flex-direction:column;gap:8px;margin-top:10px;}
  .opcion.elegida{border-color:#1e3a8a;background:#e8efff;font-weight:700;}
  .marca{display:inline-flex;gap:8px;align-items:center;margin-top:10px;font-size:15px;color:#5C3900;}
  .marca input{width:20px;height:20px;}
  .meta-q{display:block;margin-top:6px;font-size:14px;color:#4a5568;}
  .resultado{font-size:18px;margin:16px 0;padding:14px 18px;border-radius:10px;background:#eef3ff;border-left:6px solid #1e3a8a;}
  .resultado:empty{display:none;}
  table.informe{border-collapse:collapse;width:100%;margin:10px 0 18px;font-size:15px;}
  table.informe th,table.informe td{border:1px solid #c8c8c8;padding:8px 12px;text-align:left;vertical-align:top;}
  table.informe thead th{background:#26324a;color:#fff;}
  .condiciones li{margin:4px 0;}
  .solo-imp{display:none;}
  @media print{
    .lg-bar,.saltar,.barra-reloj,nav.mapa,.no-imp,#gph-calc-btn,.gph-calc,[data-gph-calculadora]{display:none !important;}
    .solo-imp{display:block;} fieldset.pregunta-c{break-inside:avoid;} body{background:#fff;}
  }"""


def pagina(items):
    L = C.L
    archivo = "social-studies/practice-test.html" if L == "en" else "es/estudios-sociales/simulacro.html"
    otro = "/es/estudios-sociales/simulacro.html" if L == "en" else "/social-studies/practice-test.html"
    datos = {"es": L == "es", "cuota": CUOTA,
             "items": [{"lec": q["lec"], "dom": q["dom"], "sp": q["sp"], "dok": q["dok"], "q": q["q"][L], "ops": q["ops"][L], "ok": q["ok"], "pistas": {int(k): v for k, v in q["pistas"][L].items()}, "sol": q["sol"][L]} for q in items],
             "doms": [[a, t(b, c)] for a, b, c in DOMS], "sps": [[a, t(b, c)] for a, b, c in SP], "guia": {k: t(*v) for k, v in GUIA.items()},
             "txt": {"preg": t("Question", "Pregunta"), "de": t(" of ", " de "), "opciones": t("Answer choices for question", "Opciones de la pregunta"), "marcar": t("Mark to review later", "Marcar para revisar"),
                     "resp": t("Answered: ", "Respondidas: "), "marcadas": t("marked: ", "marcadas: "), "respondida": t("answered", "respondida"), "sinresp": t("not answered", "sin responder"), "marcada": t("marked for review", "marcada para revisar"),
                     "ritmo1": t("Pace check: at minute ", "Control de ritmo: en el minuto "), "ritmo2": t(" you should be past question ", " conviene haber pasado la pregunta "), "ritmo3": t(". Speed up and mark the hard ones to come back to.", ". Acelere y marque las difíciles para volver después."),
                     "quedan10": t("10 minutes left. Make sure every question has an answer.", "Quedan 10 minutos. Compruebe que todas las preguntas tienen respuesta."), "quedan5": t("5 minutes left.", "Quedan 5 minutos."), "quedan1": t("1 minute left.", "Queda 1 minuto."),
                     "tiempo": t("Time is up. Your test was submitted.", "Se acabó el tiempo. Su simulacro se envió."),
                     "sin1": t("You have ", "Le quedan "), "sin2": t(" questions with no answer. There is no penalty for guessing, so answer them all. Press Submit again to finish anyway.", " preguntas sin responder. No hay penalización por error, así que respóndalas todas. Pulse Enviar otra vez para terminar de todos modos."),
                     "correcto": t("Correct.", "Correcto."), "sinresp2": t("Not answered.", "Sin responder."), "incorrecto": t("Not correct.", "Incorrecto."), "leccion": t("Lesson", "Lección"),
                     "puntaje": t("Score: ", "Resultado: "), "tiempoUsado": t("time used ", "tiempo empleado "),
                     "r50": t("Under 50%: content foundations are missing, not just technique. Review the whole topics the report points to, starting with civics, which is half the test.", "Menos del 50 %: faltan bases de contenido, no solo técnica. Repase los temas completos que señala el informe, empezando por cívica, que es la mitad del examen."),
                     "r65": t("50% to 65%: the content is there and applying it fails. Go back to the linked lessons, above all 8.1 and Topics 1 and 2, and repeat the practice test in a week.", "Entre el 50 y el 65 %: el contenido está y falla la aplicación. Vuelva a las lecciones enlazadas, sobre todo a la 8.1 y a los Temas 1 y 2, y repita el simulacro en una semana."),
                     "r75": t("65% to 75%: close. Sort each mistake into the four kinds of Lesson 8.3 (content, skill, wording, time). If wording and time dominate, practice with a clock instead of studying more.", "Entre el 65 y el 75 %: cerca. Clasifique cada error en las cuatro clases de la Lección 8.3 (contenido, destreza, enunciado, tiempo). Si dominan las de enunciado y tiempo, practique con reloj en vez de estudiar más."),
                     "rmas": t("Over 75%: ready, with a margin. Review only what the report marks lower, then take the official GED Ready® practice test.", "Más del 75 %: preparado, con margen. Repase solo lo que el informe marque más bajo y después presente el GED Ready® oficial."),
                     "dominado": t("Mastered", "Dominado"), "desarrollo": t("Getting there", "En desarrollo"), "repaso": t("Needs review", "Requiere repaso"), "repase": t("Review: ", "Repase: ")}}
    titulo = t("Social Studies practice test", "Simulacro de Estudios Sociales")
    return f'''<!DOCTYPE html>
<!-- LearnGED · {t("Social studies · Timed practice test — built by tools/build_soc_simulacro.py", "Estudios sociales · Simulacro cronometrado — construido con tools/build_soc_simulacro.py")}
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · LearnGED</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{"es" if L == "en" else "en"}" href="{otro}">
<link rel="stylesheet" href="/math/practice.css">
<link rel="stylesheet" href="/science/science.css">
<link rel="stylesheet" href="/social-studies/social.css">
<style>{ESTILO}
</style>
</head>
<body data-area="ged">
{C.barra()}
<a class="saltar" href="#principal">{t("Skip to the practice test", "Saltar al simulacro")}</a>
<div class="contenedor" id="principal">
  <header class="principal">
    <div class="ruta">{t("Social studies · Topic 8 · Lesson 8.3", "Estudios sociales · Tema 8 · Lección 8.3")}</div>
    <h1>{titulo}</h1>
    <div class="meta">{t("35 questions · 70 minutes · one attempt · calculator", "35 preguntas · 70 minutos · un intento · calculadora")}</div>
  </header>
  <p class="solo-imp" id="nombre-imp"></p>

  <section id="antes">
    <h2>{t("Before you start", "Antes de empezar")}</h2>
    <ul class="condiciones">
      <li>{t("<strong>35 questions</strong>, chosen at random from the GED-style questions of Topics 3 to 8, with the test’s mix: 18 civics and government, 7 U.S. history, 5 economics, and 5 geography. Each attempt is different.", "<strong>35 preguntas</strong>, elegidas al azar entre las preguntas tipo GED de los Temas 3 a 8, con la distribución del examen: 18 de cívica y gobierno, 7 de historia de los EE. UU., 5 de economía y 5 de geografía. Cada intento es distinto.")}</li>
      <li>{t("<strong>70 minutes, no break.</strong> The clock starts when you press Start and does not stop. When time runs out, the test is submitted by itself.", "<strong>70 minutos, sin descanso.</strong> El reloj arranca al pulsar Empezar y no se detiene. Al acabarse el tiempo, el simulacro se envía solo.")}</li>
      <li>{t("<strong>Allowed:</strong> the on-screen calculator (button at the top of the page). Nothing else: no notes, no lessons, no phone.", "<strong>Material permitido:</strong> la calculadora en pantalla (botón en la parte superior). Nada más: ni apuntes, ni lecciones, ni teléfono.")}</li>
      <li>{t("<strong>Pace:</strong> at minute 35, be at question 17 or 18. Keep the last ten minutes for marked questions.", "<strong>Ritmo:</strong> en el minuto 35, vaya por la pregunta 17 o 18. Deje los últimos diez minutos para las marcadas.")}</li>
      <li>{t("<strong>Never leave a question blank.</strong> There is no penalty for a wrong answer.", "<strong>Nunca deje una pregunta en blanco.</strong> No hay penalización por error.")}</li>
      <li>{t("This practice test uses multiple-choice questions. Practice the other item types (drag and drop, drop-down, fill in the blank, hot spot) on the <a href=\"practice-8-3.html\">practice page of Lesson 8.3</a>. It is not scored like the official test, which reports a scaled score.", "Este simulacro usa preguntas de opción múltiple. Practique los demás formatos (arrastrar y soltar, menú desplegable, completar espacios, punto en una imagen) en la <a href=\"practica-8-3.html\">página de práctica de la Lección 8.3</a>. No se califica como el examen oficial, que da una puntuación en escala.")}</li>
    </ul>
    <p>{t("Do it in real conditions: a quiet place, seventy minutes in a row, and let people at home know not to interrupt you. Before you look at your score, write down how you think you did.", "Hágalo en condiciones reales: un lugar tranquilo, setenta minutos seguidos, y avise en casa de que no lo interrumpan. Antes de mirar el resultado, anote cómo cree que le fue.")}</p>
    <p><label for="nombre"><strong>{t("Your name (optional, for the printed report)", "Su nombre (opcional, para el informe impreso)")}</strong></label><br><input type="text" id="nombre" autocomplete="name" style="font-size:17px;padding:8px;border:2px solid #b0bec5;border-radius:8px;max-width:360px;width:100%;"></p>
    <p><button class="btn" type="button" id="b-empezar">{t("Start the 70-minute practice test", "Empezar el simulacro de 70 minutos")}</button></p>
  </section>

  <section id="examen" hidden>
    <div class="barra-reloj" role="region" aria-label="{t("Timer", "Reloj")}" id="reloj-caja" tabindex="-1">
      <span>{t("Time left", "Tiempo restante")}: <span class="reloj" id="reloj" aria-hidden="false">70:00</span></span>
      <span id="contador" aria-live="off"></span>
      <button type="button" class="btn-env" id="b-enviar">{t("Submit", "Enviar")}</button>
    </div>
    <div class="aviso-reloj" id="aviso-reloj" role="alert"></div>
    <nav class="mapa no-imp" id="mapa" aria-label="{t("Go to a question", "Ir a una pregunta")}"></nav>
    <div id="preguntas"></div>
    <div class="resultado" id="resultado" tabindex="-1" role="status"></div>
    <section id="informe" hidden>
      <h2>{t("Your performance report", "Su informe de desempeño")}</h2>
      <h3>{t("By content area", "Por dominio de contenido")}</h3>
      <table class="informe"><caption class="cap-oculto">{t("Correct answers by content area", "Aciertos por dominio de contenido")}</caption><thead><tr><th scope="col">{t("Area", "Dominio")}</th><th scope="col">{t("Correct", "Aciertos")}</th><th scope="col">%</th></tr></thead><tbody id="t-dom"></tbody></table>
      <h3>{t("By social studies practice", "Por práctica de estudios sociales")}</h3>
      <p>{t("Two people with the same score can need opposite reviews. This table shows where your mistakes are concentrated and what to review.", "Dos personas con la misma puntuación pueden necesitar repasos opuestos. Esta tabla muestra dónde se concentran sus errores y qué conviene repasar.")}</p>
      <table class="informe"><caption class="cap-oculto">{t("Correct answers by social studies practice, with what to review", "Aciertos por práctica de estudios sociales, con lo que conviene repasar")}</caption><thead><tr><th scope="col">{t("Practice", "Práctica")}</th><th scope="col">{t("Correct", "Aciertos")}</th><th scope="col">%</th><th scope="col">{t("What it means and what to review", "Qué indica y qué repasar")}</th></tr></thead><tbody id="t-sp"></tbody></table>
      <p>{t("<strong>Read this report twice:</strong> once by domain, and once by what you were asked to do. If you missed questions from different domains that all asked you to compare sources or read a graph, the problem is a skill, not the content. <strong>How to review a mistake:</strong> do not just look at the right answer. Ask yourself <em>why the one you chose looked right</em>. There is almost always a reason, and that reason is the real mistake to fix.", "<strong>Lea este informe dos veces:</strong> una mirando el dominio y otra mirando qué le pidieron hacer. Si falló preguntas de dominios distintos que pedían comparar fuentes o leer una gráfica, el problema es de destreza, no de contenido. <strong>Cómo se revisa un error:</strong> no basta con mirar cuál era la respuesta correcta. Pregúntese <em>por qué le pareció bien la que eligió</em>. Casi siempre hay una razón, y esa razón es el error real que conviene corregir.")}</p>
      <p>{t("Before you register for the official test, also take <strong>GED Ready®</strong>, the official practice test from GED Testing Service, which tells you whether you are likely to pass.", "Antes de inscribirse en el examen oficial, conviene presentar también el <strong>GED Ready®</strong>, la prueba de práctica oficial de GED Testing Service, que indica si se está preparado para aprobar.")}</p>
    </section>
    <p class="no-imp" id="acciones-fin" hidden><button class="btn" type="button" id="b-imprimir">{t("Print or save the report as PDF", "Imprimir o guardar el informe en PDF")}</button> <button class="btn btn-sec" type="button" id="b-otra">{t("Take another practice test", "Hacer otro simulacro")}</button></p>
  </section>

  <footer class="pie">
    <p><a href="{C.lec("8-3")}">{t("Back to Lesson 8.3", "Volver a la Lección 8.3")}</a></p>
    {C.PIE[L]}
  </footer>
</div>
<script>
window.SIM = {json.dumps(datos, ensure_ascii=False)};
{LOGICA}
</script>
<script src="{t("/js/calculator.js", "/js/calculadora.js")}" data-color="#c0582f" data-hoja="no" defer></script>
</body>
</html>
''', archivo


if __name__ == "__main__":
    items = recoge()
    from collections import Counter
    print(Counter(q["dom"] for q in items))
    for lang in ("en", "es"):
        C.L = lang
        html, archivo = pagina(items)
        open(os.path.join(C.ROOT, archivo), "w", encoding="utf-8").write(html)
        print("ok", archivo)
    C.L = "en"
