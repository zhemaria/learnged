"""LearnGED · Ciencias · Simulacro cronometrado (Lección 8.3) — página en inglés y en español.
  science/practice-test.html · es/ciencias/simulacro.html
Reúne las preguntas tipo GED de las lecciones de contenido (Temas 3 a 7, más las de la 8.1 que no dependen de una tabla de la lección):
se ejecuta cada builder, se capturan sus llamadas a ciencia.ged_item y se descartan las que remiten a una sección o a otra pregunta de su lección.
Cada intento elige 40 preguntas con la distribución del examen (16 de ciencias de la vida, 16 de ciencias físicas y 8 de la Tierra y el espacio),
90 minutos con reloj, preguntas marcadas para revisar, envío automático al acabar el tiempo e informe por dominio y por práctica científica.
Uso: python3 tools/build_sci_simulacro.py  (después de construir las lecciones)
"""
import os, sys, re, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

EXCLUYE = re.compile(r"section|question \d|same table|Look again|the table in", re.I)
LECCIONES = [f"{a}-{b}" for a in range(3, 8) for b in (1, 2, 3)] + ["8-1"]
DOMINIO = {3: "life", 4: "life", 5: "physical", 6: "physical", 7: "earth", 8: "life"}
CUOTA = {"life": 16, "physical": 16, "earth": 8}


def recoge():
    orig = C.ged_item
    cap = []
    C.ged_item = lambda P, num, sp, dok, preg, ops, ok, pistas, sol: (cap.append((num, sp, dok, preg, ops, ok, pistas, sol)), orig(P, num, sp, dok, preg, ops, ok, pistas, sol))[1]
    items = []
    for n in LECCIONES:
        m = importlib.import_module("build_sci_" + n.replace("-", "_"))
        por = {}
        for lang in ("en", "es"):
            C.L = lang
            cap.clear()
            m.leccion()
            por[lang] = list(cap)
        for k, (en, es) in enumerate(zip(por["en"], por["es"])):
            if EXCLUYE.search(re.sub("<[^>]+>", " ", en[3])):
                continue
            items.append({"lec": n, "dom": DOMINIO[int(n[0])], "sp": en[1], "dok": en[2],
                          "q": {"en": en[3], "es": es[3]}, "ops": {"en": en[4], "es": es[4]}, "ok": en[5],
                          "pistas": {"en": {str(i): h for i, h in en[6].items()}, "es": {str(i): h for i, h in es[6].items()}},
                          "sol": {"en": en[7], "es": es[7]}})
    C.ged_item = orig
    C.L = "en"
    return items


SP = [("SP.1", "Reading science texts and graphics", "Comprender textos y gráficos científicos"),
      ("SP.2", "Designing investigations", "Diseñar investigaciones"),
      ("SP.3", "Reasoning from data", "Razonar a partir de datos"),
      ("SP.4", "Judging conclusions with evidence", "Evaluar conclusiones con evidencia"),
      ("SP.5", "Working with findings from several sources", "Trabajar con hallazgos de varias fuentes"),
      ("SP.6", "Expressing scientific information", "Expresar información científica"),
      ("SP.7", "Using formulas and scientific theories", "Aplicar fórmulas y teorías científicas"),
      ("SP.8", "Statistics and probability", "Estadística y probabilidad")]
GUIA = {"SP.1": ("Reading the passage is the problem, not the content: go back to the science readings and the vocabulary with roots.", "La dificultad está en la lectura del estímulo, no en el contenido: repase las lecturas científicas y el vocabulario con sus raíces."),
        "SP.6": ("Reading the passage is the problem, not the content: go back to the science readings and the vocabulary with roots.", "La dificultad está en la lectura del estímulo, no en el contenido: repase las lecturas científicas y el vocabulario con sus raíces."),
        "SP.3": ("The obstacle is working with numbers: review Topic 2 and the rearranging problems in Lessons 5.2, 6.1, and 6.2.", "El obstáculo es cuantitativo: repase el Tema 2 y los despejes de las lecciones 5.2, 6.1 y 6.2."),
        "SP.8": ("The obstacle is working with numbers: review Topic 2 and the rearranging problems in Lessons 5.2, 6.1, and 6.2.", "El obstáculo es cuantitativo: repase el Tema 2 y los despejes de las lecciones 5.2, 6.1 y 6.2."),
        "SP.4": ("You know the content but deciding what the data support is harder: review Lessons 8.1 and 7.3.", "El contenido se domina, pero cuesta decidir qué sostienen los datos: repase las lecciones 8.1 y 7.3."),
        "SP.5": ("You know the content but deciding what the data support is harder: review Lessons 8.1 and 7.3.", "El contenido se domina, pero cuesta decidir qué sostienen los datos: repase las lecciones 8.1 y 7.3."),
        "SP.2": ("The procedure is not automatic yet: review Topic 1 and the formula sheet until using it is automatic.", "Falta soltura en el procedimiento: repase el Tema 1 y la hoja de fórmulas hasta que su uso sea automático."),
        "SP.7": ("The procedure is not automatic yet: review Topic 1 and the formula sheet until using it is automatic.", "Falta soltura en el procedimiento: repase el Tema 1 y la hoja de fórmulas hasta que su uso sea automático.")}
DOMS = [("life", "Life science", "Ciencias de la vida"), ("physical", "Physical science", "Ciencias físicas"), ("earth", "Earth and space science", "Ciencias de la Tierra y el espacio")]

LOGICA = r'''
var D = window.SIM, ES = D.es, X = D.txt, TOTAL = 40, SEG = 90 * 60;
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
  [[30, 13], [60, 27]].forEach(function(h){ if (usado >= h[0] * 60 && !avisos[h[0]]){ avisos[h[0]] = 1; if (r < h[1]) anuncia(X.ritmo1 + h[0] + X.ritmo2 + h[1] + X.ritmo3); } });
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
    var q = p.q, bien = p.elegida === q.ok, sp = q.sp.slice(0, 4);
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
  $("resultado").innerHTML = X.puntaje + "<strong>" + ok + X.de + TOTAL + "</strong> (" + pct + " %) · " + X.tiempoUsado + mmss(usado) + ". " + (pct >= 70 ? X.bien70 : X.mal70);
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
    archivo = "science/practice-test.html" if L == "en" else "es/ciencias/simulacro.html"
    otro = "/es/ciencias/simulacro.html" if L == "en" else "/science/practice-test.html"
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
                     "bien70": t("A strong result. Use the report below to polish your weakest practice, then take the official GED Ready® practice test.", "Buen resultado. Use el informe de abajo para pulir su práctica más débil y después presente la prueba oficial GED Ready®."),
                     "mal70": t("Use the report below to see where your mistakes are concentrated, review those lessons, and try another practice test.", "Use el informe de abajo para ver dónde se concentran sus errores, repase esas lecciones y haga otro simulacro."),
                     "dominado": t("Mastered", "Dominado"), "desarrollo": t("Getting there", "En desarrollo"), "repaso": t("Needs review", "Requiere repaso"), "repase": t("Review: ", "Repase: ")}}
    titulo = t("Science practice test", "Simulacro de Ciencias")
    return f'''<!DOCTYPE html>
<!-- LearnGED · {t("Science · Timed practice test — built by tools/build_sci_simulacro.py", "Ciencias · Simulacro cronometrado — construido con tools/build_sci_simulacro.py")}
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
<style>{ESTILO}
</style>
</head>
<body data-area="ged">
{C.barra()}
<a class="saltar" href="#principal">{t("Skip to the practice test", "Saltar al simulacro")}</a>
<div class="contenedor" id="principal">
  <header class="principal">
    <div class="ruta">{t("Science · Topic 8 · Lesson 8.3", "Ciencias · Tema 8 · Lección 8.3")}</div>
    <h1>{titulo}</h1>
    <div class="meta">{t("40 questions · 90 minutes · one attempt · calculator and formula sheet", "40 preguntas · 90 minutos · un intento · calculadora y hoja de fórmulas")}</div>
  </header>
  <p class="solo-imp" id="nombre-imp"></p>

  <section id="antes">
    <h2>{t("Before you start", "Antes de empezar")}</h2>
    <ul class="condiciones">
      <li>{t("<strong>40 questions</strong>, chosen at random from the GED-style questions of Topics 3 to 8, with the test’s mix: 16 life science, 16 physical science, and 8 Earth and space science. Each attempt is different.", "<strong>40 preguntas</strong>, elegidas al azar entre las preguntas tipo GED de los Temas 3 a 8, con la distribución del examen: 16 de ciencias de la vida, 16 de ciencias físicas y 8 de la Tierra y el espacio. Cada intento es distinto.")}</li>
      <li>{t("<strong>90 minutes, no break.</strong> The clock starts when you press Start and does not stop. When time runs out, the test is submitted by itself.", "<strong>90 minutos, sin descanso.</strong> El reloj arranca al pulsar Empezar y no se detiene. Al acabarse el tiempo, el simulacro se envía solo.")}</li>
      <li>{t("<strong>Allowed:</strong> the on-screen calculator and the formula sheet (buttons at the top of the page). Nothing else: no notes, no lessons, no phone.", "<strong>Material permitido:</strong> la calculadora en pantalla y la hoja de fórmulas (botones en la parte superior). Nada más: ni apuntes, ni lecciones, ni teléfono.")}</li>
      <li>{t("<strong>Pace:</strong> by minute 30, try to be past question 13; by minute 60, past question 27. Mark the hard ones and come back.", "<strong>Ritmo:</strong> en el minuto 30, conviene haber pasado la pregunta 13; en el 60, la 27. Marque las difíciles y vuelva después.")}</li>
      <li>{t("<strong>Never leave a question blank.</strong> There is no penalty for a wrong answer.", "<strong>Nunca deje una pregunta en blanco.</strong> No hay penalización por error.")}</li>
      <li>{t("This practice test uses multiple-choice questions. Practice the other item types (drag and drop, drop-down, fill in the blank, hot spot) on the <a href=\"practice-8-3.html\">practice page of Lesson 8.3</a>. It is not scored like the official test, which reports a scaled score.", "Este simulacro usa preguntas de opción múltiple. Practique los demás formatos (arrastrar y soltar, menú desplegable, completar espacios, punto en una imagen) en la <a href=\"practica-8-3.html\">página de práctica de la Lección 8.3</a>. No se califica como el examen oficial, que da una puntuación en escala.")}</li>
    </ul>
    <p>{t("Do it in real conditions: a quiet place, ninety minutes in a row, and let people at home know not to interrupt you.", "Hágalo en condiciones reales: un lugar tranquilo, noventa minutos seguidos, y avise en casa de que no lo interrumpan.")}</p>
    <p><label for="nombre"><strong>{t("Your name (optional, for the printed report)", "Su nombre (opcional, para el informe impreso)")}</strong></label><br><input type="text" id="nombre" autocomplete="name" style="font-size:17px;padding:8px;border:2px solid #b0bec5;border-radius:8px;max-width:360px;width:100%;"></p>
    <p><button class="btn" type="button" id="b-empezar">{t("Start the 90-minute practice test", "Empezar el simulacro de 90 minutos")}</button></p>
  </section>

  <section id="examen" hidden>
    <div class="barra-reloj" role="region" aria-label="{t("Timer", "Reloj")}" id="reloj-caja" tabindex="-1">
      <span>{t("Time left", "Tiempo restante")}: <span class="reloj" id="reloj" aria-hidden="false">90:00</span></span>
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
      <h3>{t("By science practice", "Por práctica científica")}</h3>
      <p>{t("Two people with the same score can need opposite reviews. This table shows where your mistakes are concentrated and what to review.", "Dos personas con la misma puntuación pueden necesitar repasos opuestos. Esta tabla muestra dónde se concentran sus errores y qué conviene repasar.")}</p>
      <table class="informe"><caption class="cap-oculto">{t("Correct answers by science practice, with what to review", "Aciertos por práctica científica, con lo que conviene repasar")}</caption><thead><tr><th scope="col">{t("Practice", "Práctica")}</th><th scope="col">{t("Correct", "Aciertos")}</th><th scope="col">%</th><th scope="col">{t("What it means and what to review", "Qué indica y qué repasar")}</th></tr></thead><tbody id="t-sp"></tbody></table>
      <p>{t("<strong>How to review a mistake:</strong> do not just look at the right answer. Ask yourself <em>why the one you chose looked right</em>. There is almost always a reason, and that reason is the real mistake to fix.", "<strong>Cómo se revisa un error:</strong> no basta con mirar cuál era la respuesta correcta. Pregúntese <em>por qué le pareció bien la que eligió</em>. Casi siempre hay una razón, y esa razón es el error real que conviene corregir.")}</p>
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
<script src="{t("/js/calculator.js", "/js/calculadora.js")}" data-color="#c0582f" defer></script>
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
