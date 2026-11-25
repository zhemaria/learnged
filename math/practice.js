
/* LearnGED · practice engine (shared by all math practice pages)
   Feedback philosophy (as in Lumi): first mistake → a hint and another try;
   second mistake → the answer, explained. Praise the strategy, not the person. */
function $(id){ return document.getElementById(id); }
/* Language of the page: <html lang="es"> → Spanish texts; anything else → English */
var ES = (document.documentElement.lang || "").toLowerCase().indexOf("es") === 0;
var TX = ES ? {
  resueltos: function(t, p, n){ return "Resueltos: " + t + " de " + n + " (" + p + " al primer intento)"; },
  bien: "✓ Correcto. ", todavia: "<strong>Todavía no.</strong> ", otraVez: " <strong>Inténtelo de nuevo.</strong>",
  asi: "<strong>Así se resuelve.</strong> ", noEsta: "<strong>Esta vez no.</strong> ", nuevo: " Pulse <em>Otro ejercicio</em> para intentar uno más.",
  unoMas: " <strong>Tiene un intento más.</strong>", entero: "Escriba un número entero, solo con cifras (puede separar los miles con una coma).",
  revise: "Revise su respuesta una vez más."
} : {
  resueltos: function(t, p, n){ return "Solved: " + t + " of " + n + " (" + p + " on the first try)"; },
  bien: "✓ Correct. ", todavia: "<strong>Not yet.</strong> ", otraVez: " <strong>Try again.</strong>",
  asi: "<strong>Here is how to solve it.</strong> ", noEsta: "<strong>Not this time.</strong> ", nuevo: " Press <em>New exercise</em> to try one more.",
  unoMas: " <strong>You have one more try.</strong>", entero: "Type a whole number using digits only (you can use commas).",
  revise: "Check your answer one more time."
};
function aleatorio(min, max){ return Math.floor(Math.random() * (max - min + 1)) + min; }
function elige(lista){ return lista[aleatorio(0, lista.length - 1)]; }
function baraja(lista){ var a = lista.slice(); for (var i = a.length - 1; i > 0; i--){ var j = aleatorio(0, i), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function f1(x){ return Math.round(x * 10) / 10; }
function linea(p, q, color, ancho){ return '<line x1="' + f1(p[0]) + '" y1="' + f1(p[1]) + '" x2="' + f1(q[0]) + '" y2="' + f1(q[1]) + '" stroke="' + (color || "#424242") + '" stroke-width="' + (ancho || 2) + '"/>'; }
function texto(p, t, tam, color, peso){ return '<text x="' + f1(p[0]) + '" y="' + f1(p[1]) + '" text-anchor="middle" dominant-baseline="middle" font-size="' + (tam || 18) + '" font-weight="' + (peso || 700) + '" fill="' + (color || "#222") + '">' + t + '</text>'; }

/* ---------- Numbers in English ---------- */
function com(n){ return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }
var ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
var TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
function under1000(n){
  var h = Math.floor(n / 100), r = n % 100, p = [];
  if (h) p.push(ONES[h] + " hundred");
  if (r){ p.push(r < 20 ? ONES[r] : TENS[Math.floor(r / 10)] + (r % 10 ? "-" + ONES[r % 10] : "")); }
  return p.join(" ");
}
/* Groups: [digits, words, group name]  (US style: no "and", commas between groups) */
function groups(n){
  var m = Math.floor(n / 1e6), t = Math.floor(n / 1000) % 1000, u = n % 1000, g = [];
  if (m) g.push([com(m), under1000(m) + " million", "millions"]);
  if (t) g.push([String(t), under1000(t) + " thousand", "thousands"]);
  if (u) g.push([String(u), under1000(u), "ones"]);
  return g;
}
function words(n){ if (n === 0) return "zero"; return groups(n).map(function(g){ return g[1]; }).join(", "); }
function cap(s){ return s.charAt(0).toUpperCase() + s.slice(1); }
var PLACE = ["ones", "tens", "hundreds", "thousands", "ten thousands", "hundred thousands", "millions", "ten millions", "hundred millions"];
var PLACE1 = ["one", "ten", "hundred", "thousand", "ten thousand", "hundred thousand", "million", "ten million", "hundred million"];

/* ---------- Numbers in Spanish (used by the pages in /es/) ---------- */
var UNI_ = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"];
var DEC_ = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"];
var CEN_ = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"];
function menosDeMil(n){
  if (n === 100) return "cien";
  var c = Math.floor(n / 100), r = n % 100, s = CEN_[c];
  if (r){ var t = r < 30 ? UNI_[r] : DEC_[Math.floor(r / 10)] + (r % 10 ? " y " + UNI_[r % 10] : ""); s = (s ? s + " " : "") + t; }
  return s;
}
function apocope(s){ return s.replace(/veintiuno$/, "veintiún").replace(/ uno$/, " un").replace(/^uno$/, "un"); }
function enLetras(n){
  if (n === 0) return "cero";
  var mill = Math.floor(n / 1e6), miles = Math.floor(n / 1000) % 1000, u = n % 1000, p = [];
  if (mill) p.push(mill === 1 ? "un millón" : apocope(menosDeMil(mill)) + " millones");
  if (miles) p.push(miles === 1 ? "mil" : apocope(menosDeMil(miles)) + " mil");
  if (u) p.push(menosDeMil(u));
  return p.join(" ").replace(/\s+/g, " ").trim();
}
/* Groups in Spanish: [digits, words, group name] */
function grupoLetras(n){
  var mill = Math.floor(n / 1e6), miles = Math.floor(n / 1000) % 1000, u = n % 1000, p = [];
  if (mill) p.push([com(mill), mill === 1 ? "un millón" : apocope(menosDeMil(mill)) + " millones", "millones"]);
  if (miles) p.push([String(miles), miles === 1 ? "mil" : apocope(menosDeMil(miles)) + " mil", "miles"]);
  if (u) p.push([String(u), menosDeMil(u), "unidades"]);
  return p;
}
var LUGARES = ["unidad", "decena", "centena", "unidad de millar", "decena de millar", "centena de millar", "unidad de millón", "decena de millón", "centena de millón"];
var LUGARES_PL = ["unidades", "decenas", "centenas", "unidades de millar", "decenas de millar", "centenas de millar", "unidades de millón", "decenas de millón", "centenas de millón"];
function p10(k){ return Math.pow(10, k); }
function leeNum(t){ var s = String(t).replace(/[\s ,]/g, "").replace(/\$/g, ""); return /^\d+$/.test(s) ? parseInt(s, 10) : null; }

/* ---------- Praise for the strategy (rotates) ---------- */
var ELOGIO = ES ? ["Trabajó paso a paso. Esa estrategia funciona.", "Buena estrategia: revisó cada parte antes de responder.", "El trabajo cuidadoso da resultado.", "Aplicó bien la regla.", "Buen trabajo: se tomó su tiempo."] : ["You worked step by step. That strategy works.", "Good strategy: you checked each part before you answered.", "Careful work pays off.", "You used the rule correctly.", "Nice work: you took your time."];
var ELOGIO2 = ES ? ["Aprovechó bien la pista.", "Buena corrección: revisó su trabajo y lo arregló.", "Los errores nos enseñan. Encontró la respuesta correcta."] : ["You used the hint well.", "Good recovery: you checked your work and fixed it.", "Mistakes help us learn. You found the right answer."];

/* ---------- Multiple choice with two tries ---------- */
function creaPracticaOM(pre, gen){
  var est = { primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0 };
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    var q, n = 0;
    do { q = gen(); n++; } while (n < 50 && !valida(q));
    est.actual = q; est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = q.enun;
    var cont = $(pre + "-opciones"); cont.innerHTML = "";
    (q.enOrden ? q.opciones.slice() : baraja(q.opciones)).forEach(function(o){
      var b = document.createElement("button");
      b.type = "button"; b.className = "opcion"; b.innerHTML = o.html;
      b.setAttribute("data-clave", o.clave);
      b.addEventListener("click", function(){ responde(b); });
      cont.appendChild(b);
    });
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function valida(q){
    var vistas = {}, hay = 0;
    q.opciones = q.opciones.filter(function(o){ if (vistas[o.clave]) return false; vistas[o.clave] = 1; return true; });
    q.opciones.forEach(function(o){ if (o.clave === q.correcta) hay++; });
    return hay === 1 && q.opciones.length >= 2;
  }
  function cierra(){
    est.resuelta = true; est.total++;
    Array.prototype.forEach.call($(pre + "-opciones").children, function(b){
      b.disabled = true;
      if (b.getAttribute("data-clave") === est.actual.correcta) b.classList.add("correcta");
    });
  }
  function responde(btn){
    if (est.resuelta || btn.disabled) return;
    var q = est.actual, clave = btn.getAttribute("data-clave"), ok = clave === q.correcta, fb = $(pre + "-fb");
    est.intentos++;
    if (ok){
      if (est.intentos === 1) est.primero++; else est.pista++;
      cierra();
      fb.className = "fb bien";
      fb.innerHTML = TX.bien + q.bien + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
    } else if (est.intentos === 1 && q.opciones.length > 2){
      btn.classList.add("incorrecta"); btn.disabled = true;
      fb.className = "fb pista";
      fb.innerHTML = TX.todavia + ((q.pistas && q.pistas[clave]) || q.pista) + TX.otraVez;
    } else {
      btn.classList.add("incorrecta");
      cierra();
      fb.className = "fb mal";
      fb.innerHTML = (q.opciones.length > 2 ? TX.asi : TX.noEsta) + q.mal + TX.nuevo;
    }
    marcador();
  }
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
}

/* ---------- Typed answer with two tries ---------- */
function creaPracticaLibre(pre, gen){
  var est = { primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0 };
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = est.actual.enun;
    $(pre + "-r").value = ""; $(pre + "-r").disabled = false; $(pre + "-r").classList.remove("error");
    $(pre + "-comprobar").disabled = false;
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function bloquea(){ $(pre + "-r").disabled = true; $(pre + "-comprobar").disabled = true; }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), res = q.evalua($(pre + "-r").value);
    $(pre + "-r").classList.toggle("error", res.estado === "invalido");
    if (res.estado === "invalido"){ fb.className = "fb pista"; fb.innerHTML = res.msg; return; }
    est.intentos++;
    if (res.estado === "bien"){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + q.solucion + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      bloquea();
    } else if (est.intentos >= 2){
      est.resuelta = true; est.total++;
      fb.className = "fb mal"; fb.innerHTML = TX.asi + q.solucion + TX.nuevo;
      bloquea();
    } else {
      fb.className = "fb pista"; fb.innerHTML = TX.todavia + res.msg + TX.unoMas;
      $(pre + "-r").focus();
    }
    marcador();
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-r").addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
}
function numN(res, pistas, general){
  return function(t){
    var v = leeNum(t);
    if (v === null) return { estado: "invalido", msg: TX.entero };
    if (v === res) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++) if (v === pistas[i].v) return { estado: "mal", msg: pistas[i].msg };
    return { estado: "mal", msg: general || TX.revise };
  };
}

/* ---------- Navigation by anchors ---------- */
function abrePorHash(){
  var h = decodeURIComponent(window.location.hash.replace("#", "")); if (!h) return;
  var el = document.getElementById(h);
  if (el && el.tagName.toLowerCase() === "details"){ el.open = true; el.scrollIntoView({ behavior: "smooth", block: "start" }); }
}
function iniciaNavegacion(){
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener("click", function(){ var el = document.getElementById(a.getAttribute("href").slice(1)); if (el && el.tagName.toLowerCase() === "details") el.open = true; });
  });
  $("abrir-todo").addEventListener("click", function(){ document.querySelectorAll("details.modulo").forEach(function(d){ d.open = true; }); });
  $("cerrar-todo").addEventListener("click", function(){ document.querySelectorAll("details.modulo").forEach(function(d){ d.open = false; }); });
  window.addEventListener("hashchange", abrePorHash);
  abrePorHash();
}


/* ---------- Column arithmetic table (addition and subtraction) ---------- */
function tablaCol(W, filas, arriba, res, act, voz){
  var h = '<table class="columna" role="img" aria-label="' + voz + '"><tbody>';
  if (arriba) h += '<tr><td></td>' + arriba.map(function(x, i){ return '<td class="lleva' + (i === act ? " act" : "") + '">' + (x || "") + '</td>'; }).join("") + '</tr>';
  filas.forEach(function(f, k){ h += '<tr' + (k === filas.length - 1 ? ' class="ultima"' : '') + '><td>' + (f.signo || "") + '</td>' + f.dig.map(function(x, i){ return '<td class="' + (i === act ? "act" : "") + (k === filas.length - 1 ? " bajo" : "") + '">' + (x === null || x === undefined ? "" : x) + '</td>'; }).join("") + '</tr>'; });
  h += '<tr><td></td>' + res.map(function(x, i){ return '<td class="raya' + (i === act ? " act" : "") + '"><strong>' + (x === null || x === undefined ? "" : x) + '</strong></td>'; }).join("") + '</tr>';
  return h + '</tbody></table>';
}
function digitos(n, W){ var s = String(n), d = []; for (var i = 0; i < W - s.length; i++) d.push(null); return d.concat(s.split("").map(Number)); }

/* ---------- Leo, the LearnGED owl (decorative: the text already says everything) ----------
   Right answer → leo-bien · first mistake (hint) → leo-piensa · solution shown → leo-pista
   The lesson header gets Leo waving. Images use alt="" so screen readers skip them. */
(function () {
  var POSE = { bien: "bien", pista: "piensa", mal: "pista" };
  function leoImg(pose, cls, size) { return '<img class="' + cls + '" src="/img/leo-' + pose + '.svg" alt="" aria-hidden="true" data-pose="' + pose + '" width="' + size + '" height="' + size + '">'; }
  window.leoImg = leoImg;
  function pon(el) {
    var pose = null;
    for (var k in POSE) if (el.classList.contains(k)) pose = POSE[k];
    var img = null;
    for (var i = 0; i < el.children.length; i++) if (el.children[i].classList.contains("leo-fb")) img = el.children[i];
    if (!pose || !el.textContent.trim()) { if (img) img.remove(); return; }
    if (img && img.getAttribute("data-pose") === pose) return;
    if (img) img.remove();
    el.insertAdjacentHTML("afterbegin", leoImg(pose, "leo-fb", 56));
  }
  document.querySelectorAll(".fb, .respuesta-int").forEach(function (el) {
    pon(el);
    new MutationObserver(function () { pon(el); }).observe(el, { childList: true, attributes: true, attributeFilter: ["class"] });
  });
  var head = document.querySelector("header.principal .envoltura-header") || document.querySelector("header.principal");
  if (head && !head.querySelector(".leo-hola")) head.insertAdjacentHTML("afterbegin", leoImg("saludo", "leo-hola", 110));
})();
